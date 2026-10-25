"""Check coherent-output channel against direct finite-bus Lindblad evolution.

This finite numerical check is not a proof of the general formulas.
Requires numpy and scipy. Fixed example: two qubits, twelve oscillator levels,
closed sinusoidal complex trajectory, loss rate 0.7, time 1.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

T = 1.0
kappa = 0.7
n = 12
v = np.array([0.25, 0.15 + 0.2j])
omega = 2 * np.pi
z = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
a = np.diag(np.sqrt(np.arange(1, n)), 1).astype(complex)
ad = a.conj().T
number = ad @ a


def f(t):
    return np.sin(np.pi * t) * np.exp(1j * omega * t)


def df(t):
    return (np.pi * np.cos(np.pi * t) + 1j * omega * np.sin(np.pi * t)) * np.exp(1j * omega * t)


def hamiltonian(t, zi):
    force = np.dot(zi, v) * (df(t) + kappa * f(t) / 2)
    return 1j * (force * ad - force.conjugate() * a)


C = 0.5 * np.outer(v.conj(), v)
K = omega * C.real
actual = np.empty((4, 4), complex)
predicted = np.empty_like(actual)
for p in range(4):
    for q in range(4):
        initial = np.zeros((n, n), complex)
        initial[0, 0] = 1

        def rhs(t, x):
            rho = x.reshape(n, n)
            derivative = -1j * (hamiltonian(t, z[p]) @ rho - rho @ hamiltonian(t, z[q]))
            derivative += kappa * (a @ rho @ ad - 0.5 * (number @ rho + rho @ number))
            return derivative.ravel()

        solution = solve_ivp(rhs, (0, T), initial.ravel(), rtol=3e-10, atol=3e-12)
        assert solution.success, solution.message
        actual[p, q] = np.trace(solution.y[:, -1].reshape(n, n))
        zp, zq = z[p], z[q]
        delta = zp - zq
        predicted[p, q] = np.exp(
            1j * (zp @ K @ zp - zq @ K @ zq)
            - kappa / 2 * delta @ C.real @ delta
            + 1j * kappa * zq @ C.imag @ zp
        )

discrepancy = float(np.max(np.abs(actual - predicted)))
print(f"Maximum channel multiplier discrepancy: {discrepancy:.12g}")
assert discrepancy < 2e-8
assert np.max(np.abs(C.imag)) > 0.01
destination = Path(__file__).parent / 'results' / 'damped_channel.json'
destination.parent.mkdir(exist_ok=True)
destination.write_text(json.dumps({
    'status': 'passed', 'oscillator_levels': n, 'kappa': kappa, 'T': T,
    'coherences_checked': 16,
    'max_channel_multiplier_error': discrepancy,
    'maximum_imaginary_gram_entry': float(np.max(np.abs(C.imag))),
    'scope': 'Finite truncated oscillator check of the exact-channel conventions, including skew phase; not a universal proof.'
}, indent=2)+'\n')

