#!/usr/bin/env python3
"""Deterministic finite checks of the common-bus gate-layer formulas.

Run without arguments to check against expected_results.json. Use --json to
print the computed summary. The general theorems are proved in ../science;
these calculations check signs, normalization, and finite examples.
"""

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np


C0 = math.pi / 8
SEED = 20261023


def weights(k, m):
    return np.arange(k, dtype=np.int64) // (4 * m) + 1


def geometric_weight(k, m):
    return math.exp(float(np.log(weights(k, m)).mean()))


def controls(k, m, duration):
    """Fourier coefficient vectors indexed by (mode, signed harmonic)."""
    coefficients = {}
    for r in range(k):
        harmonic = r // (4 * m) + 1
        slot = r % (4 * m)
        frequency_sign = 1 if slot < 2 * m else -1
        slot %= 2 * m
        mode = slot // 2
        quadrature = 1 if slot % 2 == 0 else 1j
        vector = coefficients.setdefault(
            (mode, frequency_sign * harmonic), np.zeros(2 * k, complex)
        )
        amplitude = math.sqrt(2 * math.pi * C0 * harmonic) / duration
        vector[r] = quadrature * amplitude
        vector[k + r] = frequency_sign * quadrature * amplitude
    return coefficients


def phase_matrix(coefficients, duration):
    return sum(
        duration**2 * np.real(np.outer(v, v.conj())) / (2 * math.pi * n)
        for (_, n), v in coefficients.items()
    )


def spectral_action(a, m):
    """The exact prescribed-matrix expression, evaluated numerically."""
    eigenvalues = np.linalg.eigvalsh(a)
    positive = eigenvalues[eigenvalues > 0][::-1]
    negative = -eigenvalues[eigenvalues < 0]
    result = 0.0
    for values in (positive, negative):
        signed_weights = np.arange(len(values)) // (2 * m) + 1
        result += float(signed_weights @ values)
    return 2 * math.pi * result


def sign_vectors(k):
    return np.array(list(itertools.product([-1.0, 1.0], repeat=k)))


def boolean_cube(n):
    masks = np.arange(1 << n)
    return ((masks[:, None] >> np.arange(n)) & 1).astype(np.int64)


def multilinear_coefficients(values, n):
    """Boolean Mobius inversion, bit i indexing coordinate i."""
    coefficients = np.array(values, copy=True)
    for bit in range(n):
        for mask in range(1 << n):
            if mask & (1 << bit):
                coefficients[mask] -= coefficients[mask ^ (1 << bit)]
    return coefficients


def half_diamond_from_phases(phases):
    """Numerical-range formula via the shortest containing spectral arc."""
    angles = np.sort(np.mod(np.asarray(phases).ravel(), 2 * math.pi))
    gaps = np.diff(np.append(angles, angles[0] + 2 * math.pi))
    arc = max(0.0, 2 * math.pi - float(gaps.max()))
    return 1.0 if arc >= math.pi else math.sin(arc / 2)


def check_construction():
    count = 0
    phase_max = 0.0
    action_max = 0.0
    for m in range(1, 4):
        for k in range(1, 21):
            duration = 1.7
            coefficients = controls(k, m, duration)
            a = phase_matrix(coefficients, duration)
            target = np.zeros((2 * k, 2 * k))
            target[:k, k:] = C0 * np.eye(k)
            target[k:, :k] = C0 * np.eye(k)
            difference = a - target
            np.fill_diagonal(difference, 0.0)
            phase_error = float(np.abs(difference).max())
            assert phase_error < 1e-13

            action = duration**2 * sum(
                np.vdot(v, v).real for v in coefficients.values()
            )
            expected_action = math.pi**2 / 2 * float(weights(k, m).sum())
            action_error = abs(action - expected_action)
            assert action_error < 1e-10
            assert abs(spectral_action(a, m) - action) < 1e-10

            component_count = sum(
                (np.abs(v) > 0).astype(int) for v in coefficients.values()
            )
            assert np.all(component_count == 1)
            peak_squared = sum(np.abs(v)**2 for v in coefficients.values())
            harmonic_max = (k - 1) // (4 * m) + 1
            expected_peak_squared = (
                2 * math.pi * C0 * harmonic_max / duration**2
            )
            assert abs(float(peak_squared.max()) - expected_peak_squared) < 1e-13

            # Check the finite-size harmonic-sum formula independently.
            quotient, remainder = divmod(k, 4 * m)
            closed_sum = (
                4 * m * quotient * (quotient + 1) // 2
                + remainder * (quotient + 1)
            )
            assert int(weights(k, m).sum()) == closed_sum
            phase_max = max(phase_max, phase_error)
            action_max = max(action_max, action_error)
            count += 1

    return {
        "cases": count,
        "off_diagonal_phase_error_below": 1e-13,
        "action_and_spectral_formula_error_below": 1e-10,
        "single_tone_per_qubit": True,
        "example_K20_m1_action": round(math.pi**2 / 2 * 60, 6),
    }, {"construction_phase_error": phase_max, "construction_action_error": action_max}


def check_direct_integration():
    """Integrate waveforms; also form paths by cumulative quadrature."""
    cases = [(1, 1), (4, 1), (5, 1), (9, 2), (13, 3)]
    duration = 1.7
    grid = np.linspace(0.0, duration, 8193)
    dt = grid[1] - grid[0]
    quadrature_weights = np.full(len(grid), dt)
    quadrature_weights[[0, -1]] *= 0.5
    exact_path_phase_max = 0.0
    numerical_path_phase_max = 0.0
    closure_max = 0.0
    for k, m in cases:
        coefficients = controls(k, m, duration)
        u = np.zeros((m, 2 * k, len(grid)), complex)
        alpha = np.zeros_like(u)
        for (mode, n), vector in coefficients.items():
            omega = 2 * math.pi * n / duration
            oscillation = np.exp(1j * omega * grid)
            u[mode] += vector[:, None] * oscillation
            alpha[mode] += vector[:, None] * (oscillation - 1) / (1j * omega)

        numerical_alpha = np.zeros_like(u)
        numerical_alpha[:, :, 1:] = np.cumsum(
            (u[:, :, :-1] + u[:, :, 1:]) * (dt / 2), axis=-1
        )
        expected = phase_matrix(coefficients, duration)
        phase_errors = []
        for paths in (alpha, numerical_alpha):
            integral = sum(
                (paths[mode].conj() * quadrature_weights) @ u[mode].T
                for mode in range(m)
            )
            observed = (integral.imag + integral.imag.T) / 2
            phase_errors.append(float(np.abs(observed - expected).max()))
        assert phase_errors[0] < 2e-12
        assert phase_errors[1] < 2e-7

        closure_error = max(
            float(np.abs(u @ quadrature_weights).max()),
            float(np.abs(alpha[:, :, -1]).max()),
            float(np.abs(numerical_alpha[:, :, -1]).max()),
        )
        assert closure_error < 2e-12
        peak = math.sqrt(float(np.sum(np.abs(u)**2, axis=0).max()))
        expected_peak = (
            math.sqrt(2 * math.pi * C0 * math.ceil(k / (4 * m))) / duration
        )
        assert abs(peak - expected_peak) < 2e-12
        exact_path_phase_max = max(exact_path_phase_max, phase_errors[0])
        numerical_path_phase_max = max(numerical_path_phase_max, phase_errors[1])
        closure_max = max(closure_max, closure_error)

    return {
        "cases": [list(case) for case in cases],
        "grid_points": len(grid),
        "analytic_path_phase_error_below": 2e-12,
        "cumulative_quadrature_phase_error_below": 2e-7,
        "closure_error_below": 2e-12,
    }, {
        "integrated_phase_error": exact_path_phase_max,
        "cumulative_path_phase_error": numerical_path_phase_max,
        "closure_error": closure_max,
    }


def check_boolean_unwrapping():
    """Whole-layer phases with local terms, wraps, and quadratic errors."""
    rng = np.random.default_rng(SEED)
    cases = 0
    spectral_comparisons = 0
    recovery_max = 0.0
    for k in (1, 2, 3, 4):
        n = 2 * k
        x = boolean_cube(n)
        z = 1 - 2 * x
        for delta in (0.1, 0.4, 0.72):
            wrap_coefficients = np.zeros(1 << n, dtype=np.int64)
            wrap_coefficients[0] = int(rng.integers(-2, 3))
            wrap_values = np.full(len(x), wrap_coefficients[0], dtype=np.int64)
            residual_values = z @ rng.normal(size=n)
            for i in range(n):
                coefficient = int(rng.integers(-2, 3))
                wrap_coefficients[1 << i] = coefficient
                wrap_values += coefficient * x[:, i]
                for j in range(i + 1, n):
                    coefficient = int(rng.integers(-3, 4))
                    wrap_coefficients[(1 << i) | (1 << j)] = coefficient
                    wrap_values += coefficient * x[:, i] * x[:, j]
                    residual_values += float(rng.normal()) * z[:, i] * z[:, j]
            residual_values -= (residual_values.max() + residual_values.min()) / 2
            residual_values *= delta / float(np.abs(residual_values).max())

            q = 2 * math.pi * wrap_values + residual_values
            principal_residual = np.angle(np.exp(1j * q))
            recovered_wrap = np.rint((q - principal_residual) / (2 * math.pi)).astype(np.int64)
            recovered_coefficients = multilinear_coefficients(recovered_wrap, n)
            assert np.array_equal(recovered_wrap, wrap_values)
            assert np.array_equal(recovered_coefficients, wrap_coefficients)

            residual_coefficients = multilinear_coefficients(principal_residual, n)
            higher_degree_masks = [mask for mask in range(1 << n) if mask.bit_count() > 2]
            if higher_degree_masks:
                assert float(np.abs(residual_coefficients[higher_degree_masks]).max()) < 5e-10
            recovery_error = float(np.abs(principal_residual - residual_values).max())
            assert recovery_error < 5e-12
            recovery_max = max(recovery_max, recovery_error)

            r = np.empty((k, k))
            d = C0 * np.eye(k)
            for i in range(k):
                for j in range(k):
                    mask = (1 << i) | (1 << (k + j))
                    r[i, j] = residual_coefficients[mask] / 8
                    d[i, j] += math.pi * wrap_coefficients[mask] / 4
            c = d + r
            assert np.linalg.norm(r, "fro") <= delta / 2 + 1e-11
            sc = np.linalg.svd(c, compute_uv=False)
            sd = np.linalg.svd(d, compute_uv=False)
            assert np.linalg.norm(sc - sd) <= np.linalg.norm(r, "fro") + 1e-11
            assert abs(np.linalg.det(d)) >= C0**k - 1e-10

            # A is the quadratic part of target + q. The remaining constant
            # and linear terms are exactly the permitted global/local phases.
            a = np.zeros((n, n))
            for i in range(n):
                for j in range(i + 1, n):
                    mask = (1 << i) | (1 << j)
                    value = (
                        math.pi * wrap_coefficients[mask] / 4
                        + residual_coefficients[mask] / 8
                    )
                    if i < k and j == k + i:
                        value += C0
                    a[i, j] = a[j, i] = value
            assert np.max(np.abs(a[:k, k:] - c)) < 1e-12
            observed_error = half_diamond_from_phases(q)
            assert abs(observed_error - math.sin(delta)) < 5e-12

            for m in (1, 2, 3):
                w = weights(k, m)
                exact_term = C0 * k * geometric_weight(k, m)
                weighted_lower = exact_term - delta * np.linalg.norm(w) / 2
                assert float(w @ sc) >= weighted_lower - 1e-10
                assert spectral_action(a, m) >= 2 * math.pi * weighted_lower - 1e-10
                spectral_comparisons += 1
            cases += 1

    # The strict delta < pi/4 threshold is essential to the unwrapping lemma.
    # k=x1*x2*x3 is cubic, but q=2*pi*k+(pi/4)*z1*z2*z3 is quadratic.
    x = boolean_cube(3)
    z = 1 - 2 * x
    k_values = np.prod(x, axis=1)
    r_values = math.pi / 4 * np.prod(z, axis=1)
    q_values = 2 * math.pi * k_values + r_values
    assert abs(multilinear_coefficients(q_values, 3)[7]) < 1e-12
    assert multilinear_coefficients(k_values, 3)[7] == 1

    return {
        "seed": SEED,
        "quadratic_gate_cases": cases,
        "largest_qubit_count": 8,
        "residual_phase_radii": [0.1, 0.4, 0.72],
        "weighted_spectral_comparisons": spectral_comparisons,
        "integer_wrap_recovered_exactly": True,
        "Frobenius_and_Mirsky_bounds_hold": True,
        "strict_unwrapping_threshold_example": True,
    }, {"phase_lift_recovery_error": recovery_max}


def check_weight_constants():
    cases = 0
    largest_ratio = 0.0
    for m in range(1, 5):
        for k in range(1, 129):
            w = weights(k, m)
            g = geometric_weight(k, m)
            ratio = float(np.linalg.norm(w)) / (k * g)
            assert ratio <= 1 + 1e-13
            assert g >= max(1.0, k / (4 * math.e * m)) - 1e-13
            largest_ratio = max(largest_ratio, ratio)
            cases += 1
    return {"cases": cases, "largest_norm_w_over_KG": round(largest_ratio, 6)}


def check_wrapped_rank_collapse():
    """Small errors and low rank coexist, while action remains expensive."""
    cases = 0
    phase_wrap_max = 0.0
    illustrative_record = None
    for k in (2, 4, 6):
        for shear in (8, 32, 128, 1024):
            b = np.eye(k)
            for j in range(0, k, 2):
                b[j, j + 1] = 2 * shear
            assert np.array_equal(np.remainder(b, 2), np.eye(k))
            d = C0 * b
            left, singular, right = np.linalg.svd(d)
            kept = singular.copy()
            kept[k // 2:] = 0
            c = (left * kept) @ right
            residual = c - d
            signs = sign_vectors(k)
            residual_phases = 2 * signs @ residual @ signs.T
            delta = float(np.abs(residual_phases).max())
            assert delta < math.pi / 4
            assert np.linalg.norm(residual, "fro") <= delta / 2 + 1e-12
            assert np.linalg.matrix_rank(c, tol=1e-10) == k // 2

            # For even shear the exact wrap changes only global phase.
            difference = 2 * signs @ (c - C0 * np.eye(k)) @ signs.T
            global_correction = (k // 2) * math.pi * shear / 2
            principal_errors = np.angle(np.exp(1j * (difference - global_correction)))
            wrap_error = float(np.abs(principal_errors - residual_phases).max())
            assert wrap_error < 2e-10
            phase_wrap_max = max(phase_wrap_max, wrap_error)
            half_diamond = half_diamond_from_phases(difference - global_correction)
            assert abs(half_diamond - math.sin(delta)) < 2e-10

            for m in (1, 2, 3):
                w = weights(k, m)
                g = geometric_weight(k, m)
                lower = 2 * math.pi * (
                    C0 * k * g - delta * np.linalg.norm(w) / 2
                )
                uniform_lower = (
                    math.pi**2 / 4 * (1 - 4 * delta / math.pi) * k * g
                )
                c_singular = np.linalg.svd(c, compute_uv=False)
                signed_weights = np.arange(k) // (2 * m) + 1
                action = 4 * math.pi * float(signed_weights @ c_singular)
                assert action >= lower - 1e-10
                assert lower >= uniform_lower - 1e-10
                assert uniform_lower > 0
                if (k, m, shear) == (6, 1, 1024):
                    illustrative_record = {
                        "K": k,
                        "m": m,
                        "integer_shear": shear,
                        "cross_block_rank": k // 2,
                        "uniform_phase_error": round(delta, 6),
                        "half_diamond_error": round(half_diamond, 6),
                        "prescribed_matrix_action": round(action, 6),
                        "finite_size_lower_bound": round(lower, 6),
                    }
                cases += 1
    return {
        "cases": cases,
        "phase_wrap_residual_below": 2e-10,
        "illustrative_case": illustrative_record,
    }, {"phase_wrap_residual": phase_wrap_max}


def run_checks():
    construction, first_diagnostics = check_construction()
    integration, second_diagnostics = check_direct_integration()
    boolean, third_diagnostics = check_boolean_unwrapping()
    wraps, fourth_diagnostics = check_wrapped_rank_collapse()
    report = {
        "schema_version": 1,
        "status": "pass",
        "construction": construction,
        "direct_integration": integration,
        "boolean_unwrapping": boolean,
        "weight_constants": check_weight_constants(),
        "ill_conditioned_wraps": wraps,
        "scope": "Finite formula checks; the universal results are proved in science/.",
    }
    diagnostics = {
        **first_diagnostics,
        **second_diagnostics,
        **third_diagnostics,
        **fourth_diagnostics,
    }
    return report, diagnostics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the computed stable JSON summary")
    args = parser.parse_args()
    report, diagnostics = run_checks()
    if args.json:
        print(json.dumps(report, indent=2))
        return

    expected_path = Path(__file__).with_name("expected_results.json")
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    if report != expected:
        raise AssertionError("Computed summary differs from expected_results.json; inspect --json output.")
    print("PASS: 60 Fourier constructions; 5 directly integrated waveforms;")
    print("      12 Boolean gate cases; 36 wrapped rank-collapse comparisons;")
    print("      512 staircase-weight checks. Stable summary matches expected_results.json.")
    for name, value in diagnostics.items():
        print(f"{name}: {value:.3e}")


if __name__ == "__main__":
    main()
