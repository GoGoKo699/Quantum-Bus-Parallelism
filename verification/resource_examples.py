"""Reproduce the analytical resource figure and dimensionless architecture table.

Numbers are model calculations, not hardware forecasts. The lossless bounds,
the damped circle example and the fixed-K Pareto curves have different stated
domains; see science/architecture.md and science/loss_and_frontier.md.
"""
import json
import os
from pathlib import Path
import tempfile
import numpy as np

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'quantum-bus-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def matching_weights(m, buses):
    return np.ceil(np.arange(1, m + 1) / (4 * buses))


def lossless_time_interval(m, buses):
    w = matching_weights(m, buses)
    lower = np.pi / 2 * np.sqrt(np.exp(np.mean(np.log(w))))
    upper = np.pi / 2 * np.sqrt(w[-1])
    return float(lower), float(upper)


def circle_example(m=256, buses=1, kappa_over_g=1e-3):
    """All times and rates are normalized to the per-qubit coupling bound g."""
    k = matching_weights(m, buses)
    tau_each = np.pi * np.sqrt(k) / (2 * np.sqrt(1 - kappa_over_g / (4 * np.sqrt(k))))
    tau = float(max(tau_each))
    chi = float(tau * np.sum(1 / k) / 4)
    derivative_action = float(np.pi ** 2 * np.sum(k) / (2 * tau))
    drive_action = derivative_action + kappa_over_g ** 2 * chi / 4
    peak_force = (np.sqrt((2 * np.pi * k / tau) ** 2 + kappa_over_g ** 2 / 4)
                  + kappa_over_g / 2) / (4 * np.sqrt(k))
    assert np.max(peak_force) <= 1 + 1e-12
    # m is a multiple of 4*b in the table: this is a conservative bound,
    # obtained by summing the absolute displacement amplitudes in each bus.
    q = int(k[-1])
    occupancy_bound = float(16 * buses * np.sum(1 / np.sqrt(np.arange(1, q + 1))) ** 2)
    return {
        'pairs': m, 'buses': buses, 'kappa_over_g': kappa_over_g,
        'highest_harmonic': q, 'gT': tau, 'gX': chi,
        'G_over_g': drive_action,
        'highest_in_interval_angular_frequency_over_g': float(2 * np.pi * q / tau),
        'half_diamond_error_lower_bound': float(-np.expm1(-2 * kappa_over_g * chi) / 2),
        'maximum_individual_force_over_g': float(np.max(peak_force)),
        'conservative_total_peak_branch_occupation_bound': occupancy_bound
    }


def noisy_time_lower(m=256, epsilon=0.01, kappa_over_g=1e-3):
    delta = np.arcsin(2 * epsilon)
    nuclear_lower = np.pi * m / 4 - delta * np.sqrt(m)
    return float(kappa_over_g * nuclear_lower ** 2 / (m * -np.log1p(-2 * epsilon)))


def fixed_k_frontier(buses, prices, m=64, kappaT=0.1):
    # The SAME phase matrix for each b: m/2 positive and m/2 negative
    # rank-one pair blocks, each nonzero eigenvalue having magnitude pi/4.
    indices = np.ceil(np.arange(1, m // 2 + 1) / (2 * buses))
    a = (np.pi * indices) ** 2 + kappaT ** 2 / 4
    omega = np.sqrt(a[None, :] + prices[:, None])
    X_over_T = 2 * np.pi / 4 * np.sum(1 / omega, axis=1)
    G_times_T = 2 * np.pi / 4 * np.sum((2 * a[None, :] + prices[:, None]) / omega, axis=1)
    assert np.all(np.diff(X_over_T) < 0)
    assert np.all(np.diff(G_times_T) > -1e-8)
    return G_times_T, X_over_T


def main():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 10,
        'axes.spines.top': False, 'axes.spines.right': False,
        'svg.hashsalt': 'quantum-bus-congestion-v1', 'savefig.facecolor': 'white'
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.4), constrained_layout=True)
    colors = ['#185a9d', '#d66a24', '#287d63']
    counts = np.arange(1, 1025)
    for buses, color in zip((1, 8, 64), colors):
        interval = np.array([lossless_time_interval(int(m), buses) for m in counts])
        axes[0].fill_between(counts, interval[:, 0], interval[:, 1], color=color, alpha=.14)
        axes[0].plot(counts, interval[:, 1], color=color, lw=1.8, label=f'{buses} bus mode' + ('s' if buses > 1 else ''))
        axes[0].plot(counts, interval[:, 0], color=color, lw=1, ls='--')
    axes[0].set(xscale='log', yscale='log', xlabel='Independent CZ pairs, m', ylabel=r'Duration, $gT$',
                title='A  Lossless matching: lower and upper bounds')
    axes[0].legend(loc='upper left', frameon=False)
    axes[0].grid(alpha=.18, which='major')
    axes[0].text(.03, .57, 'Solid: attainable upper bound\nDashed: converse; shading: bracket',
                 ha='left', transform=axes[0].transAxes, fontsize=8.7)
    prices = np.r_[0., np.geomspace(1e-3, 1e6, 450)]
    endpoints = []
    for buses, color in zip((1, 4, 16), colors):
        G, X = fixed_k_frontier(buses, prices)
        axes[1].plot(G, X, color=color, lw=1.8, label=f'{buses} bus mode' + ('s' if buses > 1 else ''))
        axes[1].plot(G[0], X[0], 'o', color=color, ms=4)
        endpoints.append({'buses': buses, 'GT_min': float(G[0]), 'X_over_T_at_min': float(X[0])})
    axes[1].set(xscale='log', yscale='log', xlabel=r'Paid coupling action, $GT$',
                ylabel=r'Exposure, $X/T$', title='B  Exact exposure frontier for one fixed K')
    axes[1].legend(loc='upper right', frameon=False)
    axes[1].grid(alpha=.18, which='major')
    axes[1].text(.04, .05, r'$m=64$,  $\kappa T=0.1$' + '\nDots: least-action endpoints',
                 transform=axes[1].transAxes, fontsize=9)
    figures = ROOT / 'science' / 'figures'
    figures.mkdir(exist_ok=True)
    fig.savefig(figures / 'resource_frontiers.svg', metadata={'Date': None})
    # PNG is a local review artifact, not needed in the repository.
    fig.savefig(Path(tempfile.gettempdir()) / 'quantum_bus_resource_frontiers.png', dpi=170)
    plt.close(fig)
    out = {
        'model_only': True, 'damped_circle_table': [circle_example(buses=b) for b in (1, 4, 16, 64)],
        'noisy_time_converse': {'pairs': 256, 'epsilon': 0.01, 'kappa_over_g': .001,
                               'gT_lower_bound': noisy_time_lower()},
        'fixed_K_frontier_endpoints': endpoints,
        'domains': {'panel_A': 'Lossless, individual coefficient-force cap; all phase-lift converse versus a particular attaining construction.',
                   'panel_B': 'Fixed K, fixed T and kappa, no instantaneous-force cap; exact action/exposure Pareto frontier.',
                   'table': 'Damped, compensated circular pulses satisfying the individual force cap; error entries are rigorous lower bounds.'}
    }
    dest = ROOT / 'verification' / 'results' / 'resource_examples.json'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print('Saved the resource SVG and four-row damped matching example.')
    print(f'At m=256, epsilon=0.01, kappa/g=0.001: necessary gT >= {noisy_time_lower():.7f}')


if __name__ == '__main__':
    main()
