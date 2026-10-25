# Reproduce the finite checks

These calculations support conventions, attaining controls and the resource example. They do not replace the analytical proofs of universal bounds, establish a device forecast, or certify a full noisy-gate optimum.

## Environment and one-command run

Use Python 3.11 or later; the recorded checks used Python 3.12.14. The versions pinned in [requirements.txt](requirements.txt) are NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The scripts require no network access after dependency installation. Numerical outputs are written to [results/](results/). The resource figure is regenerated at [science/figures/resource_frontiers.svg](../science/figures/resource_frontiers.svg). Matplotlib's temporary cache and the review PNG are created in the operating system's temporary directory. No credentials or hardware services are used.

Each script can also be run directly from the repository root. An assertion failure produces a nonzero exit status. Floating-point last digits can differ by platform; the tolerances below define success, rather than bitwise equality of output files.

## What each check tests

| Command | Independent calculation | Assertion and observed scale |
|---|---|---|
| `python3 verification/check_matching.py` | Integrates five explicit matching controls with different pair/mode counts, including both quadratures, both signs, multiple harmonics and incomplete final groups. Checks all phase-matrix entries, closure, exposure, constant total power and individual peak caps. Enumerates the smallest gates after their local corrections. | Phase, closure, cost and power residuals below $`10^{-9}`$; observed maximum phase error about $`1.4\times10^{-15}`$. |
| `python3 verification/check_spectral_frontier.py` | Reconstructs a general real $`8\times8`$ phase matrix with positive, negative and zero eigenvalues using six combinations of mode count, damping and exposure price. Independently diagonalizes a finite-difference generalized area operator. | Phase/exposure residuals below $`10^{-9}`$ and force-action residual below $`10^{-8}`$; observed phase error below $`4.5\times10^{-15}`$. Leading-spectrum relative error falls from about $`2.04\times10^{-3}`$ to $`5.15\times10^{-4}`$ when the grid is doubled. |
| `python3 verification/check_damped_channel.py` | Integrates the Lindblad equation directly for all 16 two-qubit coherences and a 12-level oscillator. Compares against the coherent-output channel, using a trajectory with nonzero imaginary Gram matrix. | Maximum multiplier error below $`2\times10^{-8}`$; observed error about $`1.43\times10^{-10}`$. |
| `python3 verification/resource_examples.py` | Evaluates the exact analytical bounds and frontier, regenerates the figure, and checks the peak physical force of the compensated circular example. | Peak individual force at most $`g`$ within $`10^{-12}`$; monotone exposure/action curves; the stated noisy duration converse is $`gT\geq7.7915984`$ for the specified example. |

The actual numeric records are [matching.json](results/matching.json), [spectral_frontier.json](results/spectral_frontier.json), [damped_channel.json](results/damped_channel.json), and [resource_examples.json](results/resource_examples.json).

## Why these checks matter

The matching integration catches missing factors of two in the physical $`ZZ`$ angle and checks that the constructive action bound does not hide a total or individual peak-force violation. The spectral reconstruction tests the real multiplicity $`2b`$ and the simultaneous use of positive and negative modes; the finite-difference spectrum supplies a calculation different from substituting the analytical eigenfunctions. The direct Lindblad integration checks the damping-rate convention and the easily omitted skew bath phase.

The oscillator calculation is a finite, low-excitation truncation. Its agreement supports the stated example, not a universal truncation theorem. The finite-difference spectrum is a convergence check, not a proof of spectral completeness. That proof is given in [loss_and_frontier.md](../science/loss_and_frontier.md). The gate-level phase-lift and fixed-error statements are proved in [matching.md](../science/matching.md), not inferred from a finite set of matrices.

The figure is a deterministic evaluation of established formulas. Panel A uses the all-phase-lift converse and a particular lossless construction under individual force caps. Panel B fixes the same full $`K`$ across mode counts and imposes no pointwise cap. The damped table uses compensated circular paths and reports error lower bounds. These domains must remain distinct when reusing the numbers.

## Proof route

The mathematical chain is [model and resources](../science/model.md) → [spectral cost](../science/spectral_cost.md) → [phase lifts and robustness](../science/matching.md), with [loss and exposure](../science/loss_and_frontier.md) supplying the noisy channel and paid frontier. [Architecture](../science/architecture.md) combines them with explicit physical qualifications.
