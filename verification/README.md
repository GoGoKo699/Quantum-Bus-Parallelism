# Finite verification

The [scientific route](../science/README.md) maps the analytical results to their proofs. This directory checks explicit constructions, phase and error conventions, spectral controls, damped channels and resource examples. The computations support finite ingredients; the universal theorems rest on the written proofs.

## Run

Use Python 3.11 or later with the dependencies in [requirements.txt](requirements.txt). The checked environment is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The commands above are relative to the repository root. The runner also works from another directory. A normal run checks the lossless gates, resource bounds, spectral frontier and damped channel, compares [expected_results.json](expected_results.json) and [expected_supplemental.json](expected_supplemental.json), and regenerates [the resource figure](../science/figures/resource_frontiers.svg). It prints numerical residuals for inspection. Use `--no-figure` to execute every mathematical check without rewriting the SVG.

The checks share one Fourier-control engine. The gate cases are recorded in `expected_results.json`; the resource, loss and frontier cases are in `expected_supplemental.json`. The table below states each calculation's domain and purpose.

To inspect the computed stable summaries alone, run:

```sh
python verification/verify_bus.py --json
python verification/run_all.py --json --no-figure
```

There is no network access after dependency installation. Random coefficients use fixed seeds `20261023`, `20261024`, or `20261025`. Illustrative floating-point results in the summaries are rounded to six decimal places; assertions use explicit tolerances. Printed residuals can vary slightly with the numerical library and platform.

## What is checked

| Calculation | Instances | Check and purpose |
|---|---:|---|
| Fourier slot construction | $`K=1,\ldots,20`$, $`m=1,2,3`$; 60 cases | Every desired cross entry is $`\pi/8`$, unwanted off-diagonal terms vanish, each qubit has one tone, and the action agrees with both the harmonic sum and the prescribed-matrix spectral expression. |
| Direct waveform integration | $`(K,m)=(1,1),(4,1),(5,1),(9,2),(13,3)`$ | Integrate the phase area using the analytic displacement primitive, then independently obtain that primitive by cumulative trapezoidal integration of the force. Check the phase sign, normalization, closure, and peak force. |
| Small Boolean gate layers | $`K=1,2,3,4`$ and phase radii $`0.1,0.4,0.72`$; 12 cases | Add integer quadratic wraps and quadratic residuals with constant, local, within-side, and cross terms. Recover the integer wrap from principal phases, check its degree, recover the cross residual, and verify the Frobenius, Mirsky, weighted-action, and spectral-arc formulas. There are 36 comparisons across $`m=1,2,3`$. |
| Staircase weights | $`K=1,\ldots,128`$, $`m=1,2,3,4`$; 512 cases | Check the finite-size inequalities $`\lVert w\rVert_2\le KG_{K,m}`$ and $`G_{K,m}\ge\max\{1,K/(4em)\}`$. Their proofs cover all integers, independently of this range. |
| Ill-conditioned phase wraps | $`K=2,4,6`$, integer shear $`8,32,128,1024`$, $`m=1,2,3`$; 36 comparisons | Truncate the small singular values of unimodular blocks $`\left(\begin{smallmatrix}1&2h\\0&1\end{smallmatrix}\right)`$. Verify rank reduction, small whole-layer error after phase wrapping, and the fixed-error action lower bound. |
| Matching resources | $`(K,m)=(1,1),(3,1),(9,1),(11,2),(9,4)`$ | Reuse the Fourier engine to integrate exposure, check constant total power and individual peak force, enumerate the small gates after local corrections, and verify attainment of the sharp $`4\pi\sum_jw_js_j(C)`$ action. |
| Sharp cross-block completion | Dense rectangular $`13\times11`$ cross block; $`m=1,2,3`$ | Reconstruct three attaining signed completions, spanning multiple harmonic weights. Compare 24 additional random same-side completions with the sharp bound. |
| Stronger fixed-error estimates | 36 odd-lift perturbation cases; 1,024 scalar comparisons through $`K=256`$ | Check the weighted singular-value perturbation bound for Frobenius-small cross-block errors and the positive uniform combination on both sides of the proof's convenient $`K=30`$ split. These algebraic perturbations are not asserted to arise from whole-layer errors of the same radius. |
| General phase/exposure frontier | Real $`8\times8`$ matrix with positive, negative, and zero eigenvalues; six combinations of mode count, damping, and exposure price | Integrate the attaining trajectories and independently diagonalize a finite-difference area operator on grids of 120 and 240 interior points. |
| Vacuum-loss channel | Two qubits; 12 oscillator levels; 16 coherences | Integrate the Lindblad equation directly and compare every channel multiplier with the coherent-output formula. The nonzero imaginary trajectory Gram matrix produces a detectable phase; dropping it fails this example. |
| Physical resource examples | Four damped matching examples; three lossless duration brackets; three fixed-matrix frontier curves | Check compensated peak force and frontier monotonicity; regenerate the figure and compare the rounded model table. The stated noisy duration converse is $`gT\ge7.7915984`$ for $`K=256`$, $`\epsilon=0.01`$, $`\kappa/g=0.001`$. |

The Boolean checks also include the exact boundary example

```math
k(x)=x_1x_2x_3,\qquad
r(z)=\frac\pi4z_1z_2z_3,\qquad
q=2\pi k+r.
```

Here $`q`$ is quadratic and $`|r|=\pi/4`$, but $`k`$ is cubic. This illustrates why the proof of quadratic integer unwrapping uses the strict inequality $`\delta<\pi/4`$. It does not show that the resource theorem fails at or beyond that threshold.

## Tolerances and expected behavior

For the explicit Fourier construction, the largest allowed off-diagonal phase discrepancy is $`10^{-13}`$ and the action discrepancy is $`10^{-10}`$. With 8,193 uniform quadrature points, the analytic-path phase integration and closure checks use $`2\times10^{-12}`$; the independently integrated path uses $`2\times10^{-7}`$ to allow the trapezoidal discretization error. The intentionally large phase wraps use a $`2\times10^{-10}`$ tolerance when comparing principal phases, because reducing large phases modulo $`2\pi`$ loses some floating-point precision.

The example with $`K=6`$, $`m=1`$, and shear 1,024 has a cross block of rank three while its whole-layer phase radius is about $`0.00115`$. Its prescribed-matrix action is approximately $`4.04\times10^4`$, well above the finite-size converse. The example demonstrates the limitation of a rank-only approximate argument; it is not an efficient gate synthesis.

The universal first-harmonic approximation proposition in [matching construction, Section 6](../science/matching_construction.md#6-a-boundary-of-the-exact-harmonic-capacity-law) uses growing triangular integer matrices. Its proof is exact and does not rely on numerically resolving their increasingly ill-conditioned singular values. The numerical illustration instead uses the smaller shear blocks to avoid treating unstable floating-point ranks as evidence for that general proposition.

The matching-resource residuals are below $`10^{-9}`$ (observed total-power variation about $`1.4\times10^{-14}`$); the sharp completion residual is below $`10^{-10}`$. Frontier phase/exposure errors must be below $`10^{-9}`$, closure below $`10^{-12}`$, and paid-force error below $`10^{-8}`$. The finite-difference leading-spectrum relative error decreases from about $`2.04\times10^{-3}`$ to $`5.15\times10^{-4}`$ on doubling the grid. The finite oscillator multiplier error must be below $`2\times10^{-8}`$; the observed discrepancy is about $`1.43\times10^{-10}`$.

The oscillator example is a low-excitation finite truncation, not a universal truncation result. Finite-difference convergence does not prove spectral completeness. Random same-side completions do not prove the all-completion inequality. The figure evaluates proved formulas: panel A compares a lossless all-phase-lift converse with a particular construction under individual force caps; panel B fixes the same full phase matrix $`A`$ across mode counts and has no instantaneous cap. The damped table reports error lower bounds rather than a full noisy-gate optimum. See [hardware resources](../science/hardware_resources.md) for these distinct domains.
