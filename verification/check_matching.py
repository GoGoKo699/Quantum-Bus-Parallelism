"""Integrate the matching pulses and check phase, closure and peak budgets.

The integrations check the explicit construction independently of its closed
cost formula. They do not prove the converse or optimize over phase lifts.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import simpson


def check(m, buses, g=1.0, points=6001):
    weights = np.ceil(np.arange(1, m + 1) / (4 * buses)).astype(int)
    T = np.pi * np.sqrt(weights[-1]) / (2 * g)
    t = np.linspace(0, T, points)
    A = np.zeros((points, buses, 2 * m), complex)
    dA = np.zeros_like(A)
    K = np.zeros((2 * m, 2 * m))
    signs = []
    for j, k in enumerate(weights):
        slot = j % (4 * buses)
        sign = 1 if slot < 2 * buses else -1
        slot %= 2 * buses
        mu, quadrature = divmod(slot, 2)
        q = np.zeros(2 * m)
        q[j], q[m + j] = 1 / np.sqrt(2), sign / np.sqrt(2)
        v = (1j ** quadrature) * q / np.sqrt(8 * k)
        omega = sign * 2 * np.pi * k / T
        A[:, mu, :] += (np.exp(1j * omega * t) - 1)[:, None] * v
        dA[:, mu, :] += (1j * omega * np.exp(1j * omega * t))[:, None] * v
        K += sign * np.pi / 4 * np.outer(q, q)
        signs.append(sign)

    # Integrate individual matrix entries without retaining a time-by-n-by-n tensor.
    quadrature = np.ones(points)
    quadrature[1:-1:2] = 4
    quadrature[2:-1:2] = 2
    quadrature *= (t[1] - t[0]) / 3
    numerical_K = np.einsum('t,tmi,tmj->ij', quadrature, A.conj(), dA).imag
    power_each = np.sum(np.abs(dA) ** 2, axis=1)
    E = simpson(np.sum(power_each, axis=1), x=t)
    X = simpson(np.sum(np.abs(A) ** 2, axis=(1, 2)), x=t)
    expected_E = np.pi ** 2 * np.sum(weights) / (2 * T)
    expected_X = T * np.sum(1 / weights) / 4
    expected_powers = np.r_[weights, weights] * np.pi ** 2 / (4 * T ** 2)

    result = {
        'pairs': m, 'buses': buses, 'T': float(T),
        'phase_matrix_error': float(np.max(np.abs(numerical_K - K))),
        'closure_error': float(np.max(np.abs(A[-1]))),
        'action_error': float(abs(E - expected_E)),
        'exposure_error': float(abs(X - expected_X)),
        'individual_power_error': float(np.max(abs(power_each - expected_powers))),
        'maximum_individual_power': float(np.max(power_each)),
        'total_power_variation': float(np.ptp(np.sum(power_each, axis=1)))
    }
    if m <= 3:
        x = ((np.arange(2 ** (2 * m))[:, None] >> np.arange(2 * m)) & 1)
        z = 1 - 2 * x
        phase = np.einsum('zi,ij,zj->z', z, K, z)
        correction = np.pi / 4 * z.sum(axis=1) + np.pi / 4 * (sum(signs) - m)
        cz_phase = np.pi * np.sum(x[:, :m] * x[:, m:], axis=1)
        result['cz_phase_after_local_corrections_error'] = float(np.max(
            np.abs(np.exp(1j * (phase - correction)) - np.exp(1j * cz_phase))))
    for key, value in result.items():
        if key.endswith('error') or key == 'total_power_variation':
            assert value < 1e-9, (key, value)
    assert result['maximum_individual_power'] <= g ** 2 + 1e-12
    return result


if __name__ == '__main__':
    out = {
        'status': 'passed',
        'checks': [check(m, b) for m, b in [(1, 1), (3, 1), (9, 1), (11, 2), (9, 4)]],
        'scope': 'Explicit pulse phase/closure/instantaneous-force checks; no finite check proves the phase-lift lower bound.'
    }
    dest = Path(__file__).parent / 'results' / 'matching.json'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print('PASS: five matching constructions, including quadrature packing and multiple harmonics.')
    print('Maximum phase error:', max(c['phase_matrix_error'] for c in out['checks']))
