"""Reproduce the analytical resource figure and dimensionless architecture table.

Numbers are model calculations, not hardware forecasts. The lossless bounds,
the damped circle example and the fixed-A Pareto curves have different stated
domains; see science/hardware_resources.md and science/loss_and_frontier.md.
"""
import os
from pathlib import Path
import tempfile
import numpy as np

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'quantum-bus-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def matching_weights(K, m):
    return np.ceil(np.arange(1, K + 1) / (4 * m))


def lossless_time_interval(K, m):
    w = matching_weights(K, m)
    lower = np.pi / 2 * np.sqrt(np.exp(np.mean(np.log(w))))
    upper = np.pi / 2 * np.sqrt(w[-1])
    return float(lower), float(upper)


def circle_example(K=256, m=1, kappa_over_g=1e-3):
    """All times and rates are normalized to the per-qubit coupling bound g."""
    k = matching_weights(K, m)
    tau_each = np.pi * np.sqrt(k) / (2 * np.sqrt(1 - kappa_over_g / (4 * np.sqrt(k))))
    tau = float(max(tau_each))
    chi = float(tau * np.sum(1 / k) / 4)
    derivative_action = float(np.pi ** 2 * np.sum(k) / (2 * tau))
    drive_action = derivative_action + kappa_over_g ** 2 * chi / 4
    peak_force = (np.sqrt((2 * np.pi * k / tau) ** 2 + kappa_over_g ** 2 / 4)
                  + kappa_over_g / 2) / (4 * np.sqrt(k))
    assert np.max(peak_force) <= 1 + 1e-12
    # K is a multiple of 4*m in the table: this is a conservative bound,
    # obtained by summing the absolute displacement amplitudes in each bus.
    q = int(k[-1])
    occupancy_bound = float(16 * m * np.sum(1 / np.sqrt(np.arange(1, q + 1))) ** 2)
    return {
        'pairs': K, 'modes': m, 'kappa_over_g': kappa_over_g,
        'highest_harmonic': q, 'gT': tau, 'gX': chi,
        'paid_force_action_over_g': drive_action,
        'highest_in_interval_angular_frequency_over_g': float(2 * np.pi * q / tau),
        'half_diamond_error_lower_bound': float(-np.expm1(-2 * kappa_over_g * chi) / 2),
        'maximum_individual_force_over_g': float(np.max(peak_force)),
        'conservative_total_peak_branch_occupation_bound': occupancy_bound
    }


def noisy_time_lower(K=256, epsilon=0.01, kappa_over_g=1e-3):
    delta = np.arcsin(2 * epsilon)
    nuclear_lower = np.pi * K / 4 - delta * np.sqrt(K)
    return float(kappa_over_g * nuclear_lower ** 2 / (K * -np.log1p(-2 * epsilon)))


def fixed_matrix_frontier(modes, prices, pairs=64, kappaT=0.1):
    # The SAME phase matrix A for each mode count: K/2 positive and K/2 negative
    # rank-one pair blocks, each nonzero eigenvalue having magnitude pi/4.
    indices = np.ceil(np.arange(1, pairs // 2 + 1) / (2 * modes))
    a = (np.pi * indices) ** 2 + kappaT ** 2 / 4
    omega = np.sqrt(a[None, :] + prices[:, None])
    X_over_T = 2 * np.pi / 4 * np.sum(1 / omega, axis=1)
    G_times_T = 2 * np.pi / 4 * np.sum((2 * a[None, :] + prices[:, None]) / omega, axis=1)
    assert np.all(np.diff(X_over_T) < 0)
    assert np.all(np.diff(G_times_T) > -1e-8)
    return G_times_T, X_over_T


def run_checks(regenerate_figure=True):
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 10,
        'axes.spines.top': False, 'axes.spines.right': False,
        'svg.hashsalt': 'quantum-bus-parallelism-v1', 'savefig.facecolor': 'white'
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.4), constrained_layout=True)
    colors = ['#185a9d', '#d66a24', '#287d63']
    counts = np.arange(1, 1025)
    for modes, color in zip((1, 8, 64), colors):
        interval = np.array([lossless_time_interval(int(pairs), modes) for pairs in counts])
        axes[0].fill_between(counts, interval[:, 0], interval[:, 1], color=color, alpha=.14)
        axes[0].plot(counts, interval[:, 1], color=color, lw=1.8, label=f'{modes} bus mode' + ('s' if modes > 1 else ''))
        axes[0].plot(counts, interval[:, 0], color=color, lw=1, ls='--')
    axes[0].set(xscale='log', yscale='log', xlabel='Independent CZ pairs, K', ylabel=r'Duration, $gT$',
                title='A  Lossless matching: lower and upper bounds')
    axes[0].legend(loc='upper left', frameon=False)
    axes[0].grid(alpha=.18, which='major')
    axes[0].text(.03, .57, 'Solid: attainable upper bound\nDashed: converse; shading: bracket',
                 ha='left', transform=axes[0].transAxes, fontsize=8.7)
    prices = np.r_[0., np.geomspace(1e-3, 1e6, 450)]
    endpoints = []
    for modes, color in zip((1, 4, 16), colors):
        G, X = fixed_matrix_frontier(modes, prices)
        axes[1].plot(G, X, color=color, lw=1.8, label=f'{modes} bus mode' + ('s' if modes > 1 else ''))
        axes[1].plot(G[0], X[0], 'o', color=color, ms=4)
        endpoints.append({'modes': modes, 'paid_action_times_T_min': float(G[0]), 'X_over_T_at_min': float(X[0])})
    axes[1].set(xscale='log', yscale='log', xlabel=r'Paid coupling action, $\mathcal{E}T$',
                ylabel=r'Exposure, $X/T$', title='B  Exact exposure frontier for one fixed A')
    axes[1].legend(loc='upper right', frameon=False)
    axes[1].grid(alpha=.18, which='major')
    axes[1].text(.04, .05, r'$K=64$,  $\kappa T=0.1$' + '\nDots: least-action endpoints',
                 transform=axes[1].transAxes, fontsize=9)
    figures = ROOT / 'science' / 'figures'
    if regenerate_figure:
        figures.mkdir(exist_ok=True)
        svg = figures / 'resource_frontiers.svg'
        fig.savefig(svg, metadata={'Date': None})
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    plt.close(fig)
    out = {
        'model_only': True, 'damped_circle_table': [circle_example(m=b) for b in (1, 4, 16, 64)],
        'noisy_time_converse': {'pairs': 256, 'epsilon': 0.01, 'kappa_over_g': .001,
                               'gT_lower_bound': noisy_time_lower()},
        'fixed_A_frontier_endpoints': endpoints,
        'domains': {'panel_A': 'Lossless, individual coefficient-force cap; all phase-lift converse versus a particular attaining construction.',
                   'panel_B': 'Fixed A, fixed T and kappa, no instantaneous-force cap; exact action/exposure Pareto frontier.',
                   'table': 'Damped, compensated circular pulses satisfying the individual force cap; error entries are rigorous lower bounds.'}
    }
    # Keep stable model values in the expected summary; residuals are printed.
    def rounded(value):
        if isinstance(value, dict):
            return {key: rounded(item) for key, item in value.items()}
        if isinstance(value, list):
            return [rounded(item) for item in value]
        if isinstance(value, float):
            return round(value, 6)
        return value
    return rounded(out), {
        'maximum_compensated_force': max(row['maximum_individual_force_over_g'] for row in out['damped_circle_table']),
        'noisy_duration_converse': noisy_time_lower(),
    }


if __name__ == '__main__':
    summary, diagnostics = run_checks()
    print('PASS: physical-force examples and analytical resource frontier.')
    for name, value in diagnostics.items():
        print(f'{name}: {value:.9g}')
