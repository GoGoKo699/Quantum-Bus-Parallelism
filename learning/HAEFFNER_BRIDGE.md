# From trapped-ion gates to a shared-bus parallelism bound

Two qubits can interact by pushing a shared oscillator around a closed path. The oscillator returns, while the qubits retain a conditional phase. The question here is how the resources change when the desired operation contains many independent pairs sharing the same oscillators.

This bridge connects the selected trapped-ion review to the project's definitions, a complete one-pair example, and the additional reasoning behind its parallelism bound. A vacuum-loss continuation then shows why returning the bus does not erase information already emitted into an environment. The [30-milestone map](MILESTONES.md) organizes the broader conceptual route; the [model](../science/model.md) is the authoritative statement of assumptions and results.

## 1. The selected source and a focused reading map

**H. Häffner, C. F. Roos, and R. Blatt, “Quantum computing with trapped ions,” *Physics Reports* 469, 155–203 (2008).** [Published DOI](https://doi.org/10.1016/j.physrep.2008.09.003). The selected version is [arXiv:0809.4368v1](https://arxiv.org/abs/0809.4368v1), submitted 25 September 2008: [PDF](https://arxiv.org/pdf/0809.4368v1), [HTML](https://arxiv.org/html/0809.4368v1). All source section, figure, and equation pointers below follow the pinned v1 **PDF**; the generated HTML renumbers some equations. The bibliography key is `Haeffner2008`.

| Source location in v1 | Connection developed here |
|---|---|
| §2.2, “The basic Hamiltonian,” Eqs. (1)–(7) | Convert laser and sideband parameters to effective-force coefficients. |
| §2.6.1, “Motion of ion strings,” especially Fig. 10 | Identify the canonical modes and their participation factors. |
| §2.6.3, “Mølmer–Sørensen gate,” Eq. (15) in the PDF | Keep the spin-axis and basis conventions explicit. |
| §2.6.4, “Geometric phase gate,” especially Fig. 15 | Connect conditional forces and motional return to the closed-path model. |
| §3.1.3, “Imperfect control” | Separate the intended Hamiltonian from unwanted terms. |
| §3.2, “Motional coherence” | Distinguish endpoint closure from noise accumulated during a gate. |

These sections provide the physical entry point. The mathematical translation, worked pulse, and resource argument below use the project's conventions. The review's experimental descriptions belong to their 2008 context; the project does not use them as current hardware specifications.

## 2. Translating the physical objects into the model

### Normal modes and the meaning of the mode count

Let $`j`$ label ions and $`\ell`$ label harmonic normal modes. For identical ions, a useful notation for the displacement of ion $`j`$ along a chosen direction is

```math
\delta q_j=\sum_{\ell}b_{j\ell}x_{\mathrm{zpf},\ell}
(a_\ell+a_\ell^\dagger),
\qquad
x_{\mathrm{zpf},\ell}=\sqrt{\frac{\hbar}{2M_{\mathrm{ion}}\omega_\ell}}.
\qquad\text{(B1)}
```

Here $`b_{j\ell}`$ is the $`j`$th entry of a real normalized mode vector, $`M_{\mathrm{ion}}`$ is the ion mass, and $`a_\ell`$ removes one excitation of mode $`\ell`$. Different modes are independent canonical coordinates, with $`[a_\ell,a_k^\dagger]=\delta_{\ell k}`$. Their spatial patterns determine which ions respond to a drive and with which relative signs.

The project's $`m`$ counts these dynamical oscillator coordinates. Several modulation tones can act on the same $`a_\ell`$ without creating additional modes. Conversely, one laser envelope can couple to several different $`a_\ell`$. A mode omitted from a finite-$`m`$ description must have a justified negligible role in the interaction; calling it a spectator does not itself establish that condition. The [hardware account](../science/hardware_resources.md#2-which-modes-and-controls-count) gives the precise resource interpretation.

### From a physical drive to an inverse-time coefficient

An explicit conversion avoids ambiguity about what is being bounded. Consider a linear state-dependent potential with the sign convention

```math
H_F(t)=\sum_j F_j(t)Z_j\delta q_j,
\qquad
G_{j\ell}(t)=\frac{F_j(t)b_{j\ell}x_{\mathrm{zpf},\ell}}{\hbar}.
\qquad\text{(B2)}
```

The real quantity $`F_j`$ is the signed coefficient of the potential; the corresponding mechanical force has the opposite sign. The free-oscillator interaction picture gives

```math
\frac{H_I(t)}{\hbar}
=\sum_{j,\ell}Z_jG_{j\ell}(t)
\left(a_\ell e^{-i\omega_\ell t}
+a_\ell^\dagger e^{i\omega_\ell t}\right).
\qquad\text{(B3)}
```

This is exactly the project's convention

```math
\frac{H_I(t)}{\hbar}
=i\sum_{j,\ell}Z_j
\left(u_{j\ell}(t)a_\ell^\dagger-u_{j\ell}(t)^*a_\ell\right)
\quad\text{with}\quad
u_{j\ell}(t)=-iG_{j\ell}(t)e^{i\omega_\ell t}.
\qquad\text{(B4)}
```

Thus $`u_{j\ell}`$ has units of inverse time. This change of frame preserves its magnitude. A different sign for the potential changes the sign of $`u`$, without changing the charged force norm.

Sideband drives can produce an effective linear-force Hamiltonian through a different sequence of frame changes and approximations. The conversion is made at the level of its coefficients: if a term is written as $`Z_j[f_{j\ell}a_\ell^\dagger+f_{j\ell}^*a_\ell]`$ in $`H_I/\hbar`$, then $`u_{j\ell}=-if_{j\ell}`$. This rule is independent of how the drive amplitude was named.

| Review notation | Convention used in this project |
|---|---|
| Ion mass $`m`$ in $`z_0`$ | Write $`M_{\mathrm{ion}}`$ for mass; reserve $`m`$ for the number of modes. |
| Trap frequency $`\omega_{\mathrm t}`$ and one-mode operators $`a,a^\dagger`$ | Use $`\omega_\ell,a_\ell,a_\ell^\dagger`$ for a multimode bus. |
| $`z_0`$ and $`\eta=k_z z_0`$ | Mode participation and zero-point length enter the hardware coupling; they are absorbed into the calibrated $`u_{j\ell}`$. |
| Laser strength $`\Omega`$, detuning $`\Delta`$, and optical phase $`\varphi`$ | These determine $`u`$ after the chosen interaction picture and approximations. The force bound $`g`$ applies to the resulting coefficient, not directly to the symbol $`\Omega`$. |
| A fixed spin direction in the gate basis | Denote that Pauli operator by $`Z_j`$, with eigenvalues $`\pm1`$. A fixed change of basis is a relabeling of the model; time-dependent noncommuting spin axes change it. |

In particular, a statement such as $`g=\eta\Omega`$ needs a specified Hamiltonian normalization, drive arrangement, and mode participation. The review's Rabi-frequency convention is stated in §2.2. Reading the actual coefficient avoids importing an unintended factor of two.

### What the independent-control relaxation grants

In (B2), one function $`F_j(t)`$ determines all the mode components on ion $`j`$. An addressed laser envelope likewise generally produces components linked by participation factors and mode-dependent phases. The project instead permits each complex $`u_{j\ell}(t)`$ to be chosen independently, while charging

```math
\sum_{\ell=1}^{m}|u_{j\ell}(t)|^2\le g^2
\quad\text{for every qubit},
\qquad
\mathcal E=\int_0^T\sum_{j,\ell}|u_{j\ell}(t)|^2\,dt.
\qquad\text{(B5)}
```

This enlarged control class is useful for a converse: any hardware controls satisfying the same Hamiltonian and budget are among its admissible controls. Attaining its upper construction requires those particular complex waveforms to be physically available. The bound is on one qubit's total force across modes; assigning an independent allowance $`g`$ to every mode would increase the available total force as $`m`$ grows.

## 3. A complete one-pair closed-loop gate

Take two qubits and one harmonic mode. Fix a duration $`T>0`$ and use the equal effective forces

```math
u_1(t)=u_2(t)=\frac{i\pi}{2T}e^{2\pi it/T},
\qquad 0\le t\le T.
\qquad\text{(B6)}
```

All amplitudes in this example are Hamiltonian coefficients in (B4). The extra factor $`i`$ simply chooses the origin of the drive phase.

### The motion returns in every spin sector

Integrating either force gives

```math
\alpha_1(t)=\alpha_2(t)=\alpha(t)
=\frac{e^{2\pi it/T}-1}{4},
\qquad \alpha(0)=\alpha(T)=0.
\qquad\text{(B7)}
```

For spin eigenvalues $`z_1,z_2\in\{\pm1\}`$, the actual conditional displacement of the oscillator is

```math
\beta_z(t)=z_1\alpha_1(t)+z_2\alpha_2(t)
=(z_1+z_2)\alpha(t).
\qquad\text{(B8)}
```

Opposite spin signs give zero displacement. Equal signs give a circular path with one of two opposite displacement amplitudes. All four paths end at the origin. The final bus operator is therefore the identity in the interaction picture, for every initial bus state within the harmonic model. The pulse can entangle an initially uncorrelated bus with the spins during the path, while factorizing into a spin gate and bus identity at $`T`$.

### The closed motion leaves the required pair phase

The [closed-loop phase formula](../science/model.md#hamiltonian-and-exact-closure) gives

```math
\begin{aligned}
A_{ij}
&=\mathrm{Im}\int_0^T\alpha(t)^*\dot\alpha(t)\,dt\\
&=\mathrm{Im}\left[
\frac{i(2\pi/T)}{16}\int_0^T
\left(1-e^{2\pi it/T}\right)dt\right]
=\frac\pi8,
\qquad i,j\in\{1,2\}.
\end{aligned}
\qquad\text{(B9)}
```

Thus

```math
A=\frac\pi8\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
U_A=\exp\!\left[\frac{i\pi}{8}(Z_1+Z_2)^2\right]
=e^{i\pi/4}\exp\!\left(\frac{i\pi}{4}Z_1Z_2\right).
\qquad\text{(B10)}
```

The two diagonal entries contribute the global phase $`e^{i\pi/4}`$. The physical pair angle is **$`2A_{12}=\pi/4`$** because $`Z^{\mathsf T}AZ`$ contains both $`A_{12}Z_1Z_2`$ and $`A_{21}Z_2Z_1`$. The permitted local correction makes the controlled-$`Z`$ convention explicit:

```math
e^{-i\pi(Z_1+Z_2)/4}U_A=\mathrm{CZ}.
```

Implementing or tracking those local rotations belongs to the device resource account.

With $`Z\lvert0\rangle=\lvert0\rangle`$ and $`Z\lvert1\rangle=-\lvert1\rangle`$, the gate matrix is $`\mathrm{diag}(i,1,1,i)`$. On the product input $`\lvert++\rangle`$, where $`\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2`$, it produces

```math
U_A\lvert++\rangle
=\frac{i\lvert00\rangle+\lvert01\rangle
+\lvert10\rangle+i\lvert11\rangle}{2}.
\qquad\text{(B11)}
```

Either qubit alone has reduced state $`I/2`$, so this pure two-qubit output is maximally entangled. The qubits have retained an operation even though the bus has returned.

### The force, action, and excursion are different quantities

Each qubit's force magnitude is $`\pi/(2T)`$, and

```math
\mathcal E=2T\left(\frac\pi{2T}\right)^2
=\frac{\pi^2}{2T},
\qquad
T\mathcal E=\frac{\pi^2}{2}.
\qquad\text{(B12)}
```

The pulse meets the per-qubit bound $`g`$ by choosing $`T=\pi/(2g)`$. Its phase matrix has eigenvalues $`\pi/4`$ and zero, so its action also agrees with the [exact prescribed-matrix optimum](../science/spectral_cost.md#2-exact-minimum-for-a-prescribed-full-matrix).

The displacement satisfies $`|\alpha(t)|\le1/2`$, hence $`|\beta_z(t)|\le1`$. For an initially empty bus, the largest conditional oscillator occupation in this example is one quantum. Stretching the waveform while reducing its force inversely leaves this excursion, the phase, and $`T\mathcal E`$ unchanged. It reduces the fluence $`\mathcal E`$ and increases the duration $`T`$. Oscillator energy and force fluence therefore quantify different resources.

Collect the paths into the matrix $`D(t)=(\alpha(t),\alpha(t))`$, with one row per oscillator and one column per qubit. Its integrated squared displacement is the **exposure**

```math
X=\int_0^T\lVert D(t)\rVert_F^2dt
=2\int_0^T|\alpha(t)|^2dt=\frac T4.
```

For a vacuum bus and a uniformly sampled spin string, $`\lVert D(t)\rVert_F^2`$ is the mean conditional occupation. It is not a bound on the largest branch occupation: that maximum was one quantum here. Stretching this same loop increases $`X`$ linearly while reducing force fluence. The distinction becomes operational in the loss model below.

## 4. From one pair to independent parallel pairs

Giving the same force to every qubit produces a matrix proportional to $`\mathbf{1}\mathbf{1}^{\mathsf T}`$ and a collective phase proportional to $`(\sum_jZ_j)^2`$. That phase contains couplings between all pairs. A matching instead requires selected pairs to interact while the other pair couplings cancel, up to the allowed local phases and phase wraps.

The target for $`K`$ disjoint pairs is

```math
V_K=\prod_{r=1}^K\exp\!\left(\frac{i\pi}{4}Z_{A_r}Z_{B_r}\right).
\qquad\text{(B13)}
```

The [matching construction](../science/matching_construction.md) extends the example by assigning pair directions to mode, frequency-sign, and quadrature slots. Two real directions fit in one complex Fourier coefficient; the two frequency signs give separate signs of geometric phase. Each harmonic magnitude therefore supplies $`4m`$ slots. Additional pairs can use higher harmonics, with a corresponding action and force cost.

The full result is

```math
\mathcal A_\epsilon(K,m)=\Theta_\epsilon(K+K^2/m),
\qquad
T_\epsilon(K,m,g)=
\Theta_\epsilon\!\left(\frac{\sqrt{1+K/m}}g\right).
\qquad\text{(B14)}
```

Here $`\mathcal A_\epsilon`$ is the optimal action $`T\mathcal E`$, and $`T_\epsilon`$ is the optimal duration under (B5). The error is the half-diamond distance for the **whole layer**, optimized over final local $`Z`$ corrections. It measures worst-case distinguishability of the spin operations, including inputs entangled with a reference. For every fixed $`0\le\epsilon<1/\sqrt2`$, the constants in (B14) are independent of $`K,m,g`$. Exact conditional bus closure is required even when the allowed spin-gate error is nonzero.

At fixed force per qubit, a bounded number of modes gives a duration growing as $`\sqrt K`$. A mode budget proportional to $`K`$ permits constant-order duration in the independently controlled model. An ion chain with a growing number of available motional modes therefore need not lie in the fixed-$`m`$ regime. The mode count and the actual force budget must be established before applying the scaling law to a device.

## 5. The additional reasoning supplied by the project

The review provides the physical starting point. Four linked arguments establish the resource statement in (B14).

1. **Closed paths have an exact spectral cost.** The [spectral theorem](../science/spectral_cost.md) optimizes all square-integrable complex forces producing a full real matrix $`A`$. Its weighted eigenvalue cost counts the available directions at each harmonic. That account proves convergence for the entire control class and connects the geometry to its classical area-minimization antecedents.

2. **A physical gate has many phase-matrix representatives.** Diagonal entries change only a global phase. Shifting an off-diagonal entry by $`\pi/4`$ changes the operation by a product of local $`Z`$ operators and a global phase. The [exact gate converse](../science/gate_layer_bounds.md#2-exact-gates-force-an-odd-determinant-cross-block) addresses all such choices: the matching cross block is $`(\pi/8)(I+2M)`$ with integer $`M`$, whose determinant cannot vanish. Evaluating the cost of one chosen logarithm would leave these freedoms unexamined.

3. **Small whole-layer error preserves a quantitative constraint.** The [robust argument](../science/gate_layer_bounds.md#3-half-diamond-error-gives-a-uniform-phase-lift) controls a uniform phase error across all computational-basis strings, constrains the integer wraps, and bounds the residual cross block. A singular-value perturbation argument then preserves the action lower bound. Average fidelity or separate pairwise error guarantees do not supply this particular premise.

4. **Explicit controls attain the same order.** The [construction](../science/matching_construction.md#2-exact-action-and-force-limited-duration) realizes the matching with zero error and states its bandwidth and excursion costs. Combining this upper bound with the converse yields (B14). Finite examples in the [verification guide](../verification/README.md) check conventions and implementations; the universal bounds depend on the analytical proofs.

The source's physical foundations, these project arguments, and the research-level attributions have distinct roles. The [related-work account](../references/related_work.md) and [bibliography](../references/references.bib) identify the imported mathematical ingredients and established parallel-gate constructions. Those primary sources support attribution and specialist verification; the educational starting point remains the selected review.

## 6. Keeping the physical assumptions attached to the result

The force model is linear in oscillator coordinates and uses commuting spin axes throughout the pulse. Its exact return for arbitrary bus states is a statement about that Hamiltonian. A resonant spin–phonon exchange protocol belongs to a different Hamiltonian class unless a valid reduction to (B4) is established. A trapped-ion derivation can require harmonic confinement, a Lamb–Dicke expansion, rotating-wave approximations, and control of unwanted carrier or Stark-shift terms. Those approximations must remain valid over the actual initial occupations and driven excursions.

Endpoint closure also leaves the consequences of noise during the path intact. The fixed-error theorem in (B14) concerns a closed-bus unitary spin operation. The vacuum-loss extension below treats a separately specified noisy channel; neither statement covers residual bus displacement or an arbitrary noise process.

Finally, the increasing harmonics in the upper construction require adequate waveform control. A finite Fourier series on a pulse interval does not by itself account for switching transients or a laboratory filter. The [hardware resources page](../science/hardware_resources.md) gives these conversion and feasibility questions an explicit place alongside the ideal lower bound.

## 7. A closed loop with vacuum loss

The [loss and frontier account](../science/loss_and_frontier.md) adds uniform Markov damping at rate $`\kappa`$, with jump operators $`\sqrt{\kappa}a_\ell`$ and vacuum initial bus and reservoir. In this convention, occupation decays at rate $`\kappa`$ and amplitude at rate $`\kappa/2`$. This is a cooling-type loss process: it leaves undriven vacuum invariant. Motional heating requires a different generator and cannot be included by substituting its measured rate for $`\kappa`$.

To retain the path in (B7), rather than retain its undamped force, use $`u_i=\dot\alpha+\kappa\alpha/2`$:

```math
u_i(t)=\frac14\left[
\left(\frac{2\pi i}{T}+\frac\kappa2\right)e^{2\pi it/T}
-\frac\kappa2\right],
\qquad
\mathcal E=\frac{\pi^2}{2T}+\frac{\kappa^2T}{16}.
\qquad\text{(B15)}
```

The geometric path and pair phase remain the same, but the force budget must be checked again. The exact peak magnitude is $`[\sqrt{(2\pi/T)^2+\kappa^2/4}+\kappa/2]/4`$. The general closed-path identity is

```math
\mathcal E=E_{\mathrm{path}}+\frac{\kappa^2}{4}X,
\qquad
E_{\mathrm{path}}=\int_0^T\lVert\dot D(t)\rVert_F^2dt.
\qquad\text{(B16)}
```

Even when the damped oscillator returns to vacuum, the emitted field carries the conditional amplitude $`\sqrt{\kappa}D(t)z`$. Different spin strings can therefore leave distinguishable field states. Their overlap reduces spin coherence and can add a phase. The [exact channel](../science/loss_and_frontier.md) retains both the real and imaginary parts of $`\int D^\dagger D\,dt`$; exposure alone does not specify the channel.

This physical mechanism and ways to alter its error correlations are established in [Louis et al.](https://arxiv.org/html/0804.3240v1), §IV. [Müller, Luoma, and Strunz](https://arxiv.org/html/1907.08033v2), §III.2, Eqs. (27)–(28), explain why additional winding can lower dephasing at fixed geometric phase. The project's [paid drive–exposure frontier](../science/loss_and_frontier.md) optimizes the extra control cost for a fixed full phase matrix. It does not establish the optimum noisy channel over all phase-equivalent gates. These specialist references extend the physical discussion; the selected Häffner–Roos–Blatt review remains the educational starting point for the [30-milestone map](MILESTONES.md).
