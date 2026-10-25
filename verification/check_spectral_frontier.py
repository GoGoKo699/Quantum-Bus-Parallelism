"""Independent finite checks of the derived linear-bus spectral frontier.

Checks quadrature reconstruction of arbitrary phase matrices, exact priced
exposure constructions, and an independent finite-difference area spectrum.
These finite checks support conventions and constructions, not the proof.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import simpson
from scipy.linalg import eigh


def trajectories(K, buses, T, kappa, eta, points=12001):
    values, Q = np.linalg.eigh(K)
    t = np.linspace(0.0, T, points)
    a = np.zeros((points, buses, len(values)), dtype=complex)
    da = np.zeros_like(a)
    target_x = target_g = 0.0
    for sign in (1, -1):
        ids = [j for j in np.argsort(-sign * values) if sign * values[j] > 1e-10]
        for rank, j in enumerate(ids):
            k = rank // (2 * buses) + 1
            slot = rank % (2 * buses)
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
    Knum = simpson(np.einsum('tmi,tmj->tij', a.conj(), da), x=t, axis=0).imag
    xnum = simpson(np.sum(abs(a)**2, axis=(1, 2)), x=t)
    unum = da + kappa*a/2
    gnum = simpson(np.sum(abs(unum)**2, axis=(1, 2)), x=t)
    return {
        'buses': buses, 'T': T, 'kappa': kappa, 'eta': eta,
        'phase_matrix_error': float(np.max(abs(Knum-K))),
        'closure_error': float(max(np.max(abs(a[0])), np.max(abs(a[-1])))),
        'exposure_error': float(abs(xnum-target_x)),
        'force_action_error': float(abs(gnum-target_g)),
        'exposure': float(xnum), 'force_action': float(gnum),
    }


def difference_spectrum(points, T=1.7, lam=0.61):
    h = T/(points+1)
    D = (np.diag(np.ones(points-1), 1)-np.diag(np.ones(points-1), -1))/(2*h)
    Q = (2*np.eye(points)-np.diag(np.ones(points-1), 1)-np.diag(np.ones(points-1), -1))/h**2 + lam*np.eye(points)
    rho = eigh(-1j*D, Q, eigvals_only=True)
    observed = rho[-3:][::-1]
    expected = np.array([1/(2*np.sqrt((k*np.pi/T)**2+lam)) for k in (1, 2, 3)])
    return {'points': points, 'observed': observed.tolist(), 'expected': expected.tolist(), 'max_relative_error': float(np.max(abs(observed/expected-1)))}


def main():
    rng = np.random.default_rng(20261024)
    Q, _ = np.linalg.qr(rng.normal(size=(8, 8)))
    spectrum = np.array([2.2, 1.4, 0.8, 0.3, -1.9, -0.9, -0.2, 0.0])
    K = (Q*spectrum)@Q.T
    results = [trajectories(K, b, 1.7, kap, eta) for b in (1, 2) for kap, eta in ((0., 0.), (.7, 0.), (.7, 3.))]
    for result in results:
        assert result['phase_matrix_error'] < 1e-9, result
        assert result['closure_error'] < 1e-12, result
        assert result['exposure_error'] < 1e-9, result
        assert result['force_action_error'] < 1e-8, result
    fd = [difference_spectrum(p) for p in (120, 240)]
    assert fd[1]['max_relative_error'] < fd[0]['max_relative_error']/3
    out = {'construction_checks': results, 'finite_difference_spectrum': fd, 'status': 'passed', 'scope': 'Finite convention/construction checks only; analytical proofs remain necessary.'}
    destination = Path(__file__).parent / 'results' / 'spectral_frontier.json'
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS: six phase/frontier constructions and convergent independent area spectrum.')
    print(f'Maximum phase error: {max(x["phase_matrix_error"] for x in results):.3g}')
    print(f'Finite-difference relative errors: {[x["max_relative_error"] for x in fd]}')


if __name__ == '__main__':
    main()
