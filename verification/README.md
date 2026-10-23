# Finite verification

The analytical results are proved in [spectral cost](../science/spectral_cost.md), [gate-layer bounds](../science/gate_layer_bounds.md), and [matching construction](../science/matching_construction.md). This directory provides small, reproducible numerical checks of their normalization, constructions, and error conversions. The calculations do not establish the universal lower bound or certify a literature-priority claim.

## Run

Use Python 3.11 or later with the dependency in [requirements.txt](requirements.txt):

```sh
python -m pip install -r verification/requirements.txt
python verification/verify_bus.py
```

The commands above are relative to the repository root. The script also works from another directory because it locates its expected summary relative to its own file. A normal run checks every assertion and compares a stable summary with [expected_results.json](expected_results.json). It also prints numerical residuals for inspection. To inspect the computed summary alone, run:

```sh
python verification/verify_bus.py --json
```

There is no network access in the script. All random coefficients use the fixed seed `20261023`. Illustrative floating-point results in the summary are rounded to six decimal places; the assertions use the explicit tolerances below. The printed residuals can vary slightly with the numerical library and platform.

## What is checked

| Calculation | Instances | Check and purpose |
|---|---:|---|
| Fourier slot construction | $`K=1,\ldots,20`$, $`m=1,2,3`$; 60 cases | Every desired cross entry is $`\pi/8`$, unwanted off-diagonal terms vanish, each qubit has one tone, and the action agrees with both the harmonic sum and the prescribed-matrix spectral expression. |
| Direct waveform integration | $`(K,m)=(1,1),(4,1),(5,1),(9,2),(13,3)`$ | Integrate the phase area using the analytic displacement primitive, then independently obtain that primitive by cumulative trapezoidal integration of the force. Check the phase sign, normalization, closure, and peak force. |
| Small Boolean gate layers | $`K=1,2,3,4`$ and phase radii $`0.1,0.4,0.72`$; 12 cases | Add integer quadratic wraps and quadratic residuals with constant, local, within-side, and cross terms. Recover the integer wrap from principal phases, check its degree, recover the cross residual, and verify the Frobenius, Mirsky, weighted-action, and spectral-arc formulas. There are 36 comparisons across $`m=1,2,3`$. |
| Staircase weights | $`K=1,\ldots,128`$, $`m=1,2,3,4`$; 512 cases | Check the finite-size inequalities $`\lVert w\rVert_2\le KG_{K,m}`$ and $`G_{K,m}\ge\max\{1,K/(4em)\}`$. Their proofs cover all integers, independently of this range. |
| Ill-conditioned phase wraps | $`K=2,4,6`$, integer shear $`8,32,128,1024`$, $`m=1,2,3`$; 36 comparisons | Truncate the small singular values of unimodular blocks $`\left(\begin{smallmatrix}1&2h\\0&1\end{smallmatrix}\right)`$. Verify rank reduction, small whole-layer error after phase wrapping, and the fixed-error action lower bound. |

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
