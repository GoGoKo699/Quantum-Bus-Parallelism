"""Independent finite checks of the derived linear-bus spectral frontier.

Checks quadrature reconstruction of arbitrary phase matrices, exact priced
exposure constructions, and an independent finite-difference area spectrum.
These finite checks support conventions and constructions, not the proof.
"""
import numpy as np
from scipy.integrate import simpson
from scipy.linalg import eigh


def trajectories(A, modes, T, kappa, eta, points=12001):
    values, Q = np.linalg.eigh(A)
    t = np.linspace(0.0, T, points)
    a = np.zeros((points, modes, len(values)), dtype=complex)
    da = np.zeros_like(a)
    target_x = target_g = 0.0
    for sign in (1, -1):
        ids = [j for j in np.argsort(-sign * values) if sign * values[j] > 1e-10]
        for rank, j in enumerate(ids):
            k = rank // (2 * modes) + 1
            slot = rank % (2 * modes)
            mu, quadrature = slot // 2, slot % 2
            nu = np.pi * k / T
            abase = nu**2 + kappa**2 / 4
            omega = np.sqrt(abase + eta)
            f = np.sin(nu*t) * np.exp(1j*sign*omega*t)
            df = (nu*np.cos(nu*t) + 1j*sign*omega*np.sin(nu*t)) * np.exp(1j*sign*omega*t)
            scale = np.sqrt(2*abs(values[j])/(omega*T)) * (1j**quadrature)
            a[:, mu, :] += (scale*f)[:, None]*Q[:, j][None, :]
            da[:, mu, :] += (scale*df)[:, None]*Q[:, j][None, :]
            target_x += abs(values[j])/omega
            target_g += (2*abase+eta)*abs(values[j])/omega
    Anum = simpson(np.einsum('tmi,tmj->tij', a.conj(), da), x=t, axis=0).imag
    xnum = simpson(np.sum(abs(a)**2, axis=(1, 2)), x=t)
    unum = da + kappa*a/2
    gnum = simpson(np.sum(abs(unum)**2, axis=(1, 2)), x=t)
    return {
        'modes': modes, 'T': T, 'kappa': kappa, 'eta': eta,
        'phase_matrix_error': float(np.max(abs(Anum-A))),
        'closure_error': float(max(np.max(abs(a[0])), np.max(abs(a[-1])))),
        'exposure_error': float(abs(xnum-target_x)),
        'paid_force_error': float(abs(gnum-target_g)),
        'exposure': float(xnum), 'paid_force': float(gnum),
    }


def difference_spectrum(points, T=1.7, lam=0.61):
    h = T/(points+1)
    D = (np.diag(np.ones(points-1), 1)-np.diag(np.ones(points-1), -1))/(2*h)
    Q = (2*np.eye(points)-np.diag(np.ones(points-1), 1)-np.diag(np.ones(points-1), -1))/h**2 + lam*np.eye(points)
    rho = eigh(-1j*D, Q, eigvals_only=True)
    observed = rho[-3:][::-1]
    expected = np.array([1/(2*np.sqrt((k*np.pi/T)**2+lam)) for k in (1, 2, 3)])
    return {'points': points, 'observed': observed.tolist(), 'expected': expected.tolist(), 'max_relative_error': float(np.max(abs(observed/expected-1)))}


def run_checks():
    rng = np.random.default_rng(20261024)
    Q, _ = np.linalg.qr(rng.normal(size=(8, 8)))
    spectrum = np.array([2.2, 1.4, 0.8, 0.3, -1.9, -0.9, -0.2, 0.0])
    A = (Q*spectrum)@Q.T
    results = [trajectories(A, b, 1.7, kap, eta) for b in (1, 2) for kap, eta in ((0., 0.), (.7, 0.), (.7, 3.))]
    for result in results:
        assert result['phase_matrix_error'] < 1e-9, result
        assert result['closure_error'] < 1e-12, result
        assert result['exposure_error'] < 1e-9, result
        assert result['paid_force_error'] < 1e-8, result
    fd = [difference_spectrum(p) for p in (120, 240)]
    assert fd[1]['max_relative_error'] < fd[0]['max_relative_error']/3
    summary = {
        'phase_frontier_constructions': len(results),
        'phase_matrix_shape': [8, 8],
        'signed_nonzero_spectrum': [2.2, 1.4, 0.8, 0.3, -1.9, -0.9, -0.2],
        'phase_and_exposure_error_below': 1e-9,
        'closure_error_below': 1e-12,
        'paid_force_error_below': 1e-8,
        'finite_difference_grid_points': [120, 240],
        'spectrum_error_decreases_by_factor_above': 3,
    }
    diagnostics = {
        'frontier_phase_error': max(x['phase_matrix_error'] for x in results),
        'frontier_exposure_error': max(x['exposure_error'] for x in results),
        'frontier_paid_force_error': max(x['paid_force_error'] for x in results),
        'finite_difference_coarse_relative_error': fd[0]['max_relative_error'],
        'finite_difference_fine_relative_error': fd[1]['max_relative_error'],
    }
    return summary, diagnostics


if __name__ == '__main__':
    summary, diagnostics = run_checks()
    print('PASS: six phase/frontier constructions and convergent area spectrum.')
    for name, value in diagnostics.items():
        print(f'{name}: {value:.3e}')
