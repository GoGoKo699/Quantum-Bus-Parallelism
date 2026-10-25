"""Compare the vacuum-output channel with a finite oscillator Lindblad ODE.

This two-qubit, 12-level, low-excitation example checks all 16 multipliers,
including the imaginary trajectory Gram term. It is not a truncation theorem.
"""

import numpy as np
from scipy.integrate import solve_ivp


def run_checks():
    duration, kappa, levels = 1.0, 0.7, 12
    v = np.array([0.25, 0.15 + 0.2j])
    omega = 2 * np.pi
    z = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    a = np.diag(np.sqrt(np.arange(1, levels)), 1).astype(complex)
    ad = a.conj().T
    number = ad @ a

    def f(t):
        return np.sin(np.pi*t) * np.exp(1j*omega*t)

    def df(t):
        return (np.pi*np.cos(np.pi*t) + 1j*omega*np.sin(np.pi*t)) * np.exp(1j*omega*t)

    def hamiltonian(t, branch):
        force = np.dot(branch, v) * (df(t) + kappa*f(t)/2)
        return 1j * (force*ad - force.conjugate()*a)

    gram = .5 * np.outer(v.conj(), v)
    phase = omega * gram.real
    actual = np.empty((4, 4), complex)
    predicted = np.empty_like(actual)
    missing_skew = np.empty_like(actual)
    for p in range(4):
        for q in range(4):
            initial = np.zeros((levels, levels), complex)
            initial[0, 0] = 1

            def rhs(t, x):
                rho = x.reshape(levels, levels)
                derivative = -1j * (hamiltonian(t, z[p]) @ rho - rho @ hamiltonian(t, z[q]))
                derivative += kappa * (a @ rho @ ad - .5*(number @ rho + rho @ number))
                return derivative.ravel()

            solution = solve_ivp(rhs, (0, duration), initial.ravel(), rtol=3e-10, atol=3e-12)
            assert solution.success, solution.message
            actual[p, q] = np.trace(solution.y[:, -1].reshape(levels, levels))
            zp, zq = z[p], z[q]
            delta = zp-zq
            missing_skew[p, q] = np.exp(
                1j*(zp @ phase @ zp - zq @ phase @ zq)
                - kappa/2 * delta @ gram.real @ delta)
            predicted[p, q] = missing_skew[p, q] * np.exp(1j*kappa*zq @ gram.imag @ zp)

    discrepancy = float(np.max(abs(actual-predicted)))
    without_skew = float(np.max(abs(actual-missing_skew)))
    assert discrepancy < 2e-8
    assert float(np.max(abs(gram.imag))) > .01
    assert without_skew > .01  # This example detects accidentally dropping J.
    return {
        'oscillator_levels': levels, 'kappa': kappa, 'T': duration,
        'coherences_checked': 16, 'channel_multiplier_error_below': 2e-8,
        'nonzero_imaginary_gram_and_detectable_skew_phase': True,
    }, {'channel_multiplier_error': discrepancy,
        'channel_error_if_skew_phase_omitted': without_skew}


if __name__ == '__main__':
    summary, diagnostics = run_checks()
    print('PASS: all 16 finite-oscillator channel multipliers, including skew phase.')
    for name, value in diagnostics.items():
        print(f'{name}: {value:.3e}')
