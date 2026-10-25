"""Supplement the gate checks with peak/exposure and sharp completion checks.

The Fourier engine is the existing verify_bus module. No finite calculation
here proves the all-waveform or all-phase-lift theorem.
"""

import math

import numpy as np
from scipy.integrate import simpson

from verify_bus import C0, controls, phase_matrix, spectral_action, weights


def matching_resources():
    """Check the source's five physical-force examples using the target engine."""
    cases = [(1, 1), (3, 1), (9, 1), (11, 2), (9, 4)]
    maxima = dict(exposure_error=0.0, individual_power_error=0.0,
                  total_power_variation=0.0, local_CZ_error=0.0,
                  sharp_action_error=0.0)
    for pairs, modes in cases:
        w = weights(pairs, modes)
        duration = math.pi * math.sqrt(w[-1]) / 2
        t = np.linspace(0.0, duration, 6001)
        coefficients = controls(pairs, modes, duration)
        u = np.zeros((len(t), modes, 2 * pairs), complex)
        path = np.zeros_like(u)
        for (mode, harmonic), vector in coefficients.items():
            omega = 2 * math.pi * harmonic / duration
            oscillation = np.exp(1j * omega * t)
            u[:, mode, :] += oscillation[:, None] * vector
            path[:, mode, :] += ((oscillation - 1) / (1j * omega))[:, None] * vector
        power_each = np.sum(np.abs(u)**2, axis=1)
        exposure = simpson(np.sum(np.abs(path)**2, axis=(1, 2)), x=t)
        expected_power = np.r_[w, w] * math.pi**2 / (4 * duration**2)
        maxima['exposure_error'] = max(maxima['exposure_error'],
            float(abs(exposure - duration * np.sum(1 / w) / 4)))
        maxima['individual_power_error'] = max(maxima['individual_power_error'],
            float(np.max(abs(power_each - expected_power))))
        maxima['total_power_variation'] = max(maxima['total_power_variation'],
            float(np.ptp(np.sum(power_each, axis=1))))
        assert float(np.max(power_each)) <= 1.0 + 1e-12
        a = phase_matrix(coefficients, duration)
        # The sharp cross-block lower bound has 4*pi, and this matching attains it.
        sharp = 4 * math.pi * C0 * float(w.sum())
        maxima['sharp_action_error'] = max(maxima['sharp_action_error'],
            abs(spectral_action(a, modes) - sharp))
        if pairs <= 3:
            x = ((np.arange(2**(2*pairs))[:, None] >> np.arange(2*pairs)) & 1)
            z = 1 - 2 * x
            phases = np.einsum('zi,ij,zj->z', z, a, z)
            # Diagonal entries contribute a global phase only.
            correction = math.pi / 4 * z.sum(axis=1) + np.trace(a) - math.pi * pairs / 4
            cz_phases = math.pi * np.sum(x[:, :pairs] * x[:, pairs:], axis=1)
            error = float(np.max(abs(np.exp(1j*(phases-correction)) - np.exp(1j*cz_phases))))
            maxima['local_CZ_error'] = max(maxima['local_CZ_error'], error)
    assert max(maxima.values()) < 1e-9, maxima
    return {'cases': [list(case) for case in cases], 'grid_points': 6001,
            'residuals_below': 1e-9, 'individual_force_cap': 1.0,
            'exposure_and_constant_total_power': True,
            'sharp_cross_block_action_attained': True}, maxima


def sharp_completions():
    """Rectangular, dense cross blocks, both signs, and nontrivial staircases."""
    rng = np.random.default_rng(20261024)
    left, _ = np.linalg.qr(rng.normal(size=(13, 11)))
    right, _ = np.linalg.qr(rng.normal(size=(11, 11)))
    singular = np.array([2.2, 1.9, 1.6, 1.4, 1.1, .8, .6, .4, .3, .15, .07])
    cross = (left * singular) @ right.T
    max_error = 0.0
    sampled = 0
    for modes in (1, 2, 3):
        signs = np.where(np.arange(len(singular)) % (4*modes) < 2*modes, 1., -1.)
        directions = np.vstack((left, right * signs)) / math.sqrt(2)
        completion = (directions * (2 * signs * singular)) @ directions.T
        expected = 4 * math.pi * float(weights(len(singular), modes) @ singular)
        max_error = max(max_error, float(np.max(abs(completion[:13, 13:] - cross))),
                        abs(spectral_action(completion, modes) - expected))
        # Freely varying same-side blocks retains the cross block. These are
        # finite instances of the converse, independent of the sharp completion.
        for _ in range(8):
            trial = np.zeros((24, 24))
            trial[:13, 13:] = cross
            trial[13:, :13] = cross.T
            for start, size in ((0, 13), (13, 11)):
                block = rng.normal(size=(size, size))
                trial[start:start+size, start:start+size] = (block + block.T) / 2
            assert spectral_action(trial, modes) >= expected - 1e-10
            sampled += 1
    assert max_error < 1e-10, max_error
    return {'sharp_completions': 3, 'cross_block_shape': [13, 11],
            'sampled_other_completions': sampled, 'residual_below': 1e-10,
            'sharp_factor_4pi': True}, {'sharp_completion_error': max_error}


def fixed_error_bounds():
    """Check the sharper weighted bound and positive all-size combination."""
    rng = np.random.default_rng(20261025)
    cases = 0
    for pairs in (1, 2, 4, 8):
        for delta in (.1, .4, .72):
            # An odd-determinant exact lift plus a Frobenius-small perturbation.
            integer = rng.integers(-2, 3, size=(pairs, pairs))
            exact = C0 * (np.eye(pairs) + 2 * integer)
            perturbation = rng.normal(size=(pairs, pairs))
            perturbation *= (delta / 2) / np.linalg.norm(perturbation, 'fro')
            observed = exact + perturbation
            sv = np.linalg.svd(observed, compute_uv=False)
            eta = 4 * delta / math.pi
            factorial_root = math.exp(math.lgamma(pairs + 1) / pairs)
            q = pairs * (pairs + 1) * (2*pairs + 1) / 6
            for modes in (1, 2, 3):
                w = weights(pairs, modes)
                geometric = math.exp(float(np.log(w).mean()))
                weighted = 4 * math.pi * (C0*pairs*geometric - delta*np.linalg.norm(w)/2)
                assert 4 * math.pi * float(w @ sv) >= weighted - 1e-10
                finite = math.pi**2 / 2 * max(
                    pairs - eta * math.sqrt(pairs),
                    (pairs * factorial_root - eta * math.sqrt(q)) / (4*modes))
                uniform = math.pi**2 * (1-eta) * (pairs+pairs*pairs/modes) / 60
                assert 4 * math.pi * float(w @ sv) >= finite - 1e-10
                assert finite >= uniform - 1e-10
                cases += 1
    # Cover both sides of the proof's convenient K=30 split without forming
    # increasingly ill-conditioned matrices.
    for pairs in range(1, 257):
        eta = .96
        factorial_root = math.exp(math.lgamma(pairs+1) / pairs)
        q = pairs*(pairs+1)*(2*pairs+1)/6
        for modes in (1, 2, 7, 64):
            finite = max(pairs-eta*math.sqrt(pairs),
                         (pairs*factorial_root-eta*math.sqrt(q))/(4*modes))
            uniform = (1-eta)*(pairs+pairs*pairs/modes)/30
            assert finite >= uniform - 1e-10
    return {'weighted_perturbation_cases': cases,
            'all_size_constant_cases': 1024, 'largest_pairs': 256,
            'sharp_weighted_bound_and_positive_combination': True}


def run_checks():
    matching, first = matching_resources()
    completions, second = sharp_completions()
    return {'matching_resources': matching, 'sharp_completions': completions,
            'fixed_error_bounds': fixed_error_bounds()}, {**first, **second}
