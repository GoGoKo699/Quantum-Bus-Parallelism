# Hardware resources behind the shared-bus bound

The [model](model.md) gives a lower bound for commuting, linear, qubit-dependent forces on a finite harmonic bus. It deliberately grants more control than many devices possess. A restricted device inherits the lower bound when its Hamiltonian and force budget map into that model. The [upper construction](matching_construction.md) additionally requires particular independent controls, modulation frequencies, and oscillator excursions. Those requirements need separate checks on a proposed implementation.

Throughout, there are $`N=2K`$ participating qubits and $`m`$ canonical oscillator modes. The interaction-picture convention is

```math
H/\hbar=i\sum_{j,\ell}Z_j(u_{j\ell}a_\ell^\dagger-u_{j\ell}^*a_\ell),
\qquad
\alpha_{j\ell}(t)=\int_0^t u_{j\ell}(s)\,ds.
```

Each path closes at $`T`$. The per-qubit constraint is $`\sum_\ell|u_{j\ell}(t)|^2\le g^2`$, and $`\mathcal E=\int_0^T\sum_{j,\ell}|u_{j\ell}|^2dt`$.

| Quantity | Physical meaning | What it does not count |
|---|---|---|
| $`m`$ | Number of dynamical canonical oscillator modes available to the interaction | Number of waveform generators, tones, or time segments |
| $`g`$ | Bound on one qubit's total effective force norm across all modes; units $`\mathrm{s}^{-1}`$ | A separate allowance of $`g`$ on every mode |
| $`\mathcal E`$ | Integrated squared effective force; units $`\mathrm{s}^{-1}`$ | Device-independent electrical or optical energy |
| $`T\mathcal E`$ | Dimensionless force action | A gate count or an effective Ising interaction time |
| $`B_{\rm tone}`$ | Largest angular frequency in the construction's finite Fourier series on $`[0,T]`$ | A complete specification of switching transients or an analog filter |
| $`\lvert\beta_\ell(t)\rvert^2`$ | Added conditional oscillator occupation for a zero-mean input state | The force action or a universal occupation lower bound |

## 1. Converting a laboratory coupling to the force norm

For dimensionless quadratures $`x=(a+a^\dagger)/\sqrt2`$ and $`p=(a-a^\dagger)/(i\sqrt2)`$, with $`[x,p]=i`$,

```math
H/\hbar=\sqrt2\sum_{j,\ell}Z_j
\left[(\mathrm{Re}u_{j\ell})p_\ell
-(\mathrm{Im}u_{j\ell})x_\ell\right].
```

Thus an independent complex force means independent access to two rotating-frame quadratures. It does not mean that two independently accessible laboratory quadratures are automatically present.

For a real longitudinal resonator coupling

```math
H_{\rm lab}/\hbar=\omega_r a^\dagger a+
\sum_j G_j(t)Z_j(a+a^\dagger),
```

the exact free-oscillator interaction picture gives

```math
u_j(t)=-iG_j(t)e^{i\omega_rt},\qquad |u_j(t)|=|G_j(t)|.
\qquad\text{(H1)}
```

A physical force term $`F_j(t)Z_jx_{\rm phys}`$, where $`x_{\rm phys}=x_{\rm zpf}(a+a^\dagger)`$, has $`G_j=F_jx_{\rm zpf}/\hbar`$. The sign of the potential changes the sign of $`u_j`$ without changing its norm. Qubit-controlled electrical resonator displacements are developed explicitly in [Kerman, Sections II–III](https://arxiv.org/html/1212.3300v4).

A useful general calibration is

```math
u_j(t)=C_j(t)v_j(t),
\qquad
\|u_j(t)\|_2\le\sigma_{\max}(C_j(t))\|v_j(t)\|_2,
\qquad\text{(H2)}
```

where $`v_j`$ contains actual actuator amplitudes and $`C_j`$ includes participation factors, conversion constants, and rotating-frame phases. A restricted real domain for $`v_j`$ remains a restriction even when $`u_j`$ is complex. A usable peak-force bound follows from an upper bound on the right-hand side. The converse is valid with such a bound; achieving a desired $`u_j`$ additionally requires that it lie in the image of the calibrated actuator map with allowed amplitudes and rates of change.

For example, a single independently addressed ion drive can have effective couplings of the form

```math
u_{j\ell}(t)=b_{j\ell}\Omega_j(t)e^{i\Delta_\ell t},
\qquad
\|u_j(t)\|_2^2=|\Omega_j(t)|^2\sum_\ell|b_{j\ell}|^2,
\qquad\text{(H3)}
```

with convention-dependent constants absorbed into $`b_{j\ell}`$. Fixed normal-mode participation factors constrain all the components together. More tones enlarge the actuator map but do not generally remove those constraints. The exact hardware coefficients, rather than the schematic normalization in (H3), must be used for a numerical comparison. [Peleg et al., Section II and Appendix A](https://arxiv.org/html/2307.09566v2) formulate such a hardware-dependent multimode gate problem.

### Force fluence is not automatically energy in joules

An energy conversion requires the actual transduction chain. For an idealized scalar calibration $`u=\chi V`$ and dissipative power $`P=V^2/R`$, one would obtain $`\mathcal E=|\chi|^2R\int Pdt`$. This identity assumes the same waveform at the specified impedance and a frequency-independent calibration. Optical Raman couplings, frequency-dependent impedances, amplification losses, and shared electronics require their own conversion. The theorem makes no universal electrical or optical energy claim. Likewise, oscillator energy $`\hbar\omega_\ell\langle a_\ell^\dagger a_\ell\rangle`$ is a distinct resource.

## 2. Which modes and controls count?

A common waveform can drive many normal modes. A magnetic-gradient ion gate with one envelope can still use the full axial mode family; [Orozco-Ruiz and Mintert, Section II, Eq. (1)](https://arxiv.org/html/2602.11326v1) provides an explicit example. Counting that envelope as one bus mode would misapply the theorem. Conversely, adding many sideband tones to one resonator does not turn it into many independent canonical oscillators.

If a model consistently restricts every force to a fixed $`d`$-dimensional complex subspace of the interaction-picture mode space, a fixed passive change of basis can remove the unused coordinates. Then $`d`$ modes suffice for the mathematical description. A low instantaneous actuator rank alone does not establish such a common subspace: mode-dependent evolution can change its orientation over time.

The force budget also needs care as $`m`$ varies. Independent bounds $`|u_{j\ell}|\le g_0`$ imply $`\|u_j\|_2\le\sqrt m\,g_0`$, not $`g_0`$. Substituting $`g_0`$ for the total-force bound would give an incorrect architectural comparison.

For an ion chain that supplies a number of useful modes proportional to its number of qubits, a matching with $`K\le N/2`$ has $`K/m=O(1)`$. The finite-mode law therefore does not, by itself, predict a growing parallel-layer penalty for every long ion chain. Fixed participation, mode crowding, heating, and actuator constraints can impose other costs. A processor coupled through a bounded number of effective resonator modes is a more direct application of the few-mode regime.

A real resonator has further modes and nonlinear corrections. A finite-$`m`$ approximation must justify which degrees of freedom can actually contribute at the chosen drive amplitudes and frequencies. Unintended modes cannot be omitted merely because the control was designed for a fundamental mode; [Kerman, Appendix C](https://arxiv.org/html/1212.3300v4) treats this physical issue. The present theorem concerns the specified finite-mode Hamiltonian, rather than a general truncation theorem for an electromagnetic structure.

## 3. Bandwidth of the explicit upper construction

Let

```math
L=\left\lceil\frac K{4m}\right\rceil.
```

The [construction, Section 3](matching_construction.md#3-bandwidth-of-the-construction), derives the waveform frequencies and force-limited duration:

```math
T_{\rm force}=\frac\pi{2g}\sqrt L,
\qquad
B_{\rm tone}=\frac{2\pi L}{T_{\rm force}}=4g\sqrt L.
\qquad\text{(H4)}
```

Thus the time-optimal order at fixed $`g`$ uses increasing modulation frequencies when $`K/m`$ grows. Within this finite-tone control model, a separate maximum tone frequency $`B`$ can be respected by stretching the same construction to

```math
T\ge\max\left\{\frac\pi{2g}\sqrt L,\frac{2\pi L}{B}\right\}.
\qquad\text{(H5)}
```

The geometric phase and $`T\mathcal E`$ are unchanged by this stretching. Equation (H5) is a sufficient construction cost, not an asserted universal bandwidth-dependent optimum.

For exact gates, the finite Fourier class with harmonics $`\pm1,\ldots,\pm L`$ has capacity $`K\le4mL`$; see [construction, Section 5](matching_construction.md#5-exact-capacity-with-finitely-many-fourier-harmonics). Its [Section 6 counterexample](matching_construction.md#6-a-boundary-of-the-exact-harmonic-capacity-law) shows why exactness matters: arbitrary matching sizes can be approximated with only the two harmonics $`\pm1`$ if action is allowed to diverge. A rank-only harmonic-capacity restriction therefore does not extend to fixed nonzero error without another charged resource. Neither statement is a general result about signals passed through a physical low-pass filter.

In particular, turning a nonzero endpoint tone on and off introduces additional frequency content. The displayed $`B_{\rm tone}`$ does not include those switching transients. Smooth endpoint envelopes, finite slew rates, carrier-generation limits, and closure corrections need an implementation-specific design. A rotating-wave approximation must also remain valid over the full chosen tone range.

## 4. Oscillator excursion and noise exposure

In a computational basis sector $`z\in\{\pm1\}^{2K}`$, the displacement of mode $`\ell`$ is

```math
\beta_{\ell,z}(t)=\sum_jz_j\alpha_{j\ell}(t).
\qquad\text{(H6)}
```

The [construction, Section 4](matching_construction.md#4-displacement-and-oscillator-excursion), derives the individual-loop and collective bounds. A qubit assigned harmonic $`k`$ obeys

```math
|\alpha_{j\ell}(t)|\le\frac1{2\sqrt k}.
\qquad\text{(H7)}
```

The displacement amplitudes are independent of the overall time stretch. Filling every slot through harmonic $`L`$ gives the conservative, state-uniform bounds

```math
\max_{z,t}|\beta_{\ell,z}(t)|
\le4\sum_{k=1}^L k^{-1/2}\le8\sqrt L,
\qquad
\max_{z,t}|\beta_{\ell,z}(t)|^2\le64L.
\qquad\text{(H8)}
```

This is an upper bound for this construction, not a necessary occupation cost and not a claim that the worst phases align at one time. Partial slot filling can reduce it.

A different statistic is the uniform average over computational basis strings. For full filling of one mode,

```math
\mathbb E_z|\beta_{\ell,z}(t)|^2\le2H_L,
\qquad
\frac1T\int_0^T\mathbb E_z|\beta_{\ell,z}(t)|^2dt=H_L,
\quad H_L=\sum_{k=1}^L\frac1k.
\qquad\text{(H9)}
```

The latter grows logarithmically, whereas the bound (H8) allows larger excursions for adversarial spin strings. Neither statistic substitutes for the other in a hardware specification.

For an oscillator input with zero mean and occupation $`\bar n_\ell`$, the conditional occupation is $`\bar n_\ell+|\beta_{\ell,z}|^2`$. For nonzero initial mean it also contains $`2\mathrm{Re}[\beta_{\ell,z}^*\langle a_\ell\rangle]`$. Exact endpoint closure removes the final ideal displacement for every input state. It does not remove information already lost to an environment, nor ensure that a real device remains harmonic during the path. Photon loss during a longitudinal gate is analyzed in [Royer et al., “Oscillator-induced qubit dephasing,” Eq. (4)](https://arxiv.org/html/1603.04424v3). For trapped-ion realizations, the Lamb–Dicke approximation also constrains motional excitation; see [Leibfried et al., Section III.B.3](https://www.nist.gov/system/files/documents/2017/05/09/rmp1.pdf).

The model's statement for every oscillator input is an exact mathematical property of the harmonic Hamiltonian. It is not a claim that a physical harmonic or Lamb–Dicke approximation holds for arbitrarily high-energy initial states.

## 5. A parameterized single-resonator example

[Royer et al.](https://doi.org/10.22331/q-2017-05-11-11) study real modulation $`G_j(t)=G_j\cos(\omega_mt)`$ of longitudinal coupling. Their proposed parameter example after Fig. 2 uses $`G/2\pi=60\,\mathrm{MHz}`$, detuning $`\delta/2\pi=537\,\mathrm{MHz}`$, and a gate time about $`37\,\mathrm{ns}`$. These are theoretical example parameters, not an experimental benchmark.

Equation (H1) gives the exact force

```math
u_j(t)=-\frac{iG_j}{2}
\left[e^{i(\omega_r-\omega_m)t}+e^{i(\omega_r+\omega_m)t}\right].
\qquad\text{(H10)}
```

The physical peak in this exact expression is $`G_j`$. Retaining only the slowly varying term gives the rotating-wave envelope amplitude $`g_j=G_j/2`$. The theorem must use the budget of whichever Hamiltonian is actually being analyzed: $`G_j`$ for the exact real-force model, or $`G_j/2`$ for the ideal slow-envelope model. The two should not be interchanged.

Using the published amplitude scale only to set units, the independently programmable slow-envelope construction with $`m=1`$ and $`g/2\pi=30\,\mathrm{MHz}`$ has the following analytical requirements from (H4):

| Pairs $`K`$ | Harmonics $`L=\lceil K/4\rceil`$ | Ideal duration $`T_{\rm force}`$ | Highest envelope frequency $`B_{\rm tone}/2\pi`$ |
|---:|---:|---:|---:|
| 1 | 1 | $`8.33\,\mathrm{ns}`$ | $`120\,\mathrm{MHz}`$ |
| 4 | 1 | $`8.33\,\mathrm{ns}`$ | $`120\,\mathrm{MHz}`$ |
| 16 | 4 | $`16.67\,\mathrm{ns}`$ | $`240\,\mathrm{MHz}`$ |
| 64 | 16 | $`33.33\,\mathrm{ns}`$ | $`480\,\mathrm{MHz}`$ |

This table is a calculation in the ideal control model. It does not establish that the proposed resonator provides this many individually tunable qubits, both detuning signs and quadratures, the required waveform rates, or negligible unwanted couplings. It also does not replace the paper's different operating point. In the real drive, the fast term in (H10), its phase, and full endpoint closure must be checked; discarding it is an additional approximation.

As a normalization check, a single pair driven by equal slow forces of magnitude $`G/2`$ at detuning $`\delta`$ has $`n`$ closed windings when $`\delta T=2\pi n`$. Its $`ZZ`$ angle has magnitude $`\pi/4`$ when

```math
\delta=2G\sqrt n,\qquad T=\frac{\pi\sqrt n}{G}.
```

Taking $`n=20`$ and the same $`G`$ gives $`\delta/2\pi=536.66\,\mathrm{MHz}`$ and $`T=37.27\,\mathrm{ns}`$, consistent with the rounded example scale. In this slow-envelope calculation the largest conditional added occupation is $`1/n=0.05`$ and $`T\mathcal E=\pi^2n/2`$. These last quantities are derived here; they do not include the fast term of (H10) or dissipation.

## 6. Changes of frame and resources outside the model

Spin-independent number-preserving oscillator evolution acts by a unitary mixing of annihilation operators. In its interaction picture the force vectors undergo a unitary transformation, so $`\sum_\ell|u_{j\ell}|^2`$ and the number of canonical modes are preserved. Closure is then relative to the known net passive bus evolution. A time-dependent change of frame need not preserve the bandwidth of the laboratory actuator signals.

Active squeezing instead mixes annihilation and creation operators through a Bogoliubov transformation. It can change the Euclidean force norm and requires additional resources; it cannot be treated as free passive relabeling in this bound. Preparing a squeezed initial state alone does not change the closed-loop geometric phase, although it can change noise sensitivity and occupation. The passive/active distinction is reviewed in [Weedbrook et al., Sections II.B–II.C](https://arxiv.org/html/1110.3234v1).

Direct qubit interactions, conditional oscillator rotations such as $`Za^\dagger a`$, oscillator nonlinearities, measurements with feedback, and spin rotations that make the interaction axes noncommuting during the force evolution change the model. Sign reversals that keep the toggling-frame axis $`\pm Z`$ remain compatible with it. A claimed improvement using another interaction mechanism should be evaluated with that mechanism's own resource accounting.

For a device that satisfies the stated Hamiltonian, closure, mode-count, and total-force assumptions, the lower bound survives all further restrictions on its actuators. The scaling upper bound belongs to the independently programmable model; a hardware implementation must separately establish the required controls, bandwidth, and allowed excursions.


## 7. Independent directions and a collective phase

The matching law concerns independent phase directions. A collective rank-one matrix $`A=\chi vv^{\mathsf T}`$, with $`v_j\in\{\pm1\}`$ on $`n`$ qubits, has only one nonzero eigenvalue of magnitude $`|\chi|n`$. One mode therefore attains $`T\mathcal E=2\pi|\chi|n`$. Each qubit can obey the same fixed force cap while duration remains independent of $`n`$ at fixed $`\chi`$. This gate generally couples every pair; its cost is compatible with the matching converse.

For the separate total instantaneous cap $`\sum_{j,\ell}|u_{j\ell}(t)|^2\le P`$, the [exact matching sandwich](gate_layer_bounds.md#9-additional-finite-size-and-total-force-consequences) gives $`\inf PT^2=\Theta(K+K^2/m)`$. Under the individual cap, the total cap is at most $`P=2Kg^2`$, and the independent construction gives the sharper per-qubit feasibility check. Adding modes never grants each qubit a separate allowance of $`g`$ on every mode.

## 8. A global accuracy constraint from vacuum loss

Assume the [vacuum Markov model](loss_and_frontier.md), with common number-decay rate $`\kappa>0`$ and exactly closed actual damped paths. Suppose the actual spin channel, including allowed local $`Z`$ corrections, has half-diamond error at most

```math
0<\epsilon<\frac1{2\sqrt2},\qquad
\delta=\arcsin(2\epsilon),\qquad
L_\epsilon=-\log(1-2\epsilon).
\qquad\text{(H11)}
```

The [direct noisy phase extraction](gate_layer_bounds.md#10-direct-converse-for-the-vacuum-lossy-channel) gives $`A_{AB}=c(I+2M)+R`$, $`c=\pi/8`$, with integer $`M`$ and $`\lVert R\rVert_F\le\delta/2`$. The odd determinant and arithmetic–geometric mean imply $`\lVert c(I+2M)\rVert_*\ge\pi K/8`$. Since $`\lVert R\rVert_*\le\sqrt K\lVert R\rVert_F`$ and $`\lVert A\rVert_*\ge2\lVert A_{AB}\rVert_*`$,

```math
\lVert A\rVert_*\ge\frac{\pi K}{4}-\delta\sqrt K
=:r_{K,\epsilon}>0.
\qquad\text{(H12)}
```

Positivity follows from $`\delta<\pi/4`$ and $`K\ge1`$. Independently, the [target-independent exposure floor](loss_and_frontier.md#2-operational-error-and-first-order-gate-metrics) gives

```math
\epsilon\ge\frac{1-e^{-2\kappa X}}2,
\qquad X\le\frac{L_\epsilon}{2\kappa}.
```

The geometric inequality $`E_{\rm path}X\ge\lVert A\rVert_*^2`$, the paid cost $`\mathcal E\ge E_{\rm path}`$, and a total physical-force cap $`\mathcal E\le PT`$ therefore yield

```math
\boxed{T\ge\frac{2\kappa r_{K,\epsilon}^2}{P L_\epsilon}.}
\qquad\text{(H13)}
```

Under the individual cap $`P\le2Kg^2`$ this becomes

```math
\boxed{gT\ge\frac\kappa g
\frac{(\pi K/4-\delta\sqrt K)^2}{K L_\epsilon}.}
\qquad\text{(H14)}
```

At fixed small whole-layer error this grows linearly in $`K`$, independently of the number of modes. For small $`\epsilon`$ and large $`K`$, its leading expression is $`gT\gtrsim(\pi^2/32)(\kappa/g)K/\epsilon`$. It is a necessary condition to combine with the finite-mode bound, not a construction attaining the full noisy target. The environment receives a record of the conditional paths; adding modes does not by itself remove that record. This global worst-case error is not a local stochastic error parameter or a fault-tolerance threshold.

## 9. Duration brackets and the exposure frontier

![Lossless duration brackets and exact fixed-phase force/exposure frontiers](figures/resource_frontiers.svg)

**Panel A.** The shaded intervals bracket the lossless optimal duration under the individual cap. With $`w_r=\lceil r/(4m)\rceil`$, the necessary lower and achievable upper bounds are

```math
\frac\pi2 G_{K,m}^{1/2}\le gT_{\min}
\le\frac\pi2\sqrt{\left\lceil\frac K{4m}\right\rceil}.
```

The lower bound relaxes individual caps to their total budget and includes every phase representative. The constant gap is a converse gap, not experimental uncertainty. For $`K\le4m`$, both bounds are $`\pi/2`$.

**Panel B.** The exact $`(\mathcal E,X)`$ frontier is at fixed $`T`$ and fixed full phase matrix $`A`$, without a pointwise force cap. All curves use the same completion for $`K=64`$ pairs: 32 positive and 32 negative rank-one blocks, each with eigenvalue magnitude $`\pi/4`$. Here $`\kappa T=0.1`$. Every point is attainable in the independent-force model. Increasing the exposure price reduces $`X`$ and increases $`\mathcal E`$. More modes lower the minimum-fluence endpoint; its exposure need not decrease. The full error also depends on the environmental Gram matrix, so this is not an exact diamond-error frontier.

The [resource-examples script](../verification/resource_examples.py) reproduces the figure from analytical formulas.

## 10. A damped matching with an actual peak-force cap

Take $`K=256`$ independent pairs and the illustrative dimensionless rate $`\kappa/g=10^{-3}`$. This is a model parameter, not an estimate for a device. Pair $`r`$ uses harmonic $`n_r=\lceil r/(4m)\rceil`$ in the [compensated circular construction](matching_construction.md#7-exposure-total-force-and-compensated-damping). Its physical-force maximum, duration chosen to meet every individual cap, and exposure are

```math
\max_t|u_j(t)|=
\frac{\sqrt{(2\pi n_r/T)^2+\kappa^2/4}+\kappa/2}{4\sqrt{n_r}},
```

```math
gT=\max_r\frac{\pi\sqrt{n_r}}{2\sqrt{1-\kappa/(4g\sqrt{n_r})}},
\qquad
gX=\frac{gT}{4}\sum_{r=1}^K\frac1{n_r}.
\qquad\text{(H15)}
```

The denominator condition holds for these parameters. The limiting harmonic saturates its cap.

| Modes $`m`$ | Highest harmonic | Duration $`gT`$ | Exposure $`gX`$ | Highest in-interval angular frequency divided by $`g`$ | Rigorous half-diamond error floor |
|---:|---:|---:|---:|---:|---:|
| 1 | 64 | 12.5666 | 59.6144 | 31.9995 | 0.05620 |
| 4 | 16 | 6.2834 | 84.9696 | 15.9995 | 0.07814 |
| 16 | 4 | 3.1418 | 104.7263 | 7.9995 | 0.09449 |
| 64 | 1 | 1.5710 | 100.5435 | 3.9995 | 0.09108 |

The last column is $`(1-e^{-2\kappa X})/2`$, a lower bound for these controls rather than their exact diamond distance. Every row fails a 1% global half-diamond target. The architecture-wide converse (H14) gives $`gT\ge7.7916`$ for that target at every $`m`$. In particular, the last two short durations cannot meet the target through any other closed waveform at the same individual cap. The first row being slower than that necessary bound does not certify its accuracy; its explicit exposure rules it out.

More modes improve ideal parallelism, while a low-error design must also pay to reduce exposure. The [exact fixed-matrix frontier](loss_and_frontier.md) gives its integrated-force price. Jointly optimizing a pointwise cap and the full channel is a further control problem. The [same script](../verification/resource_examples.py) reproduces this table.

## 11. Preparation, occupation, and data memory

Vacuum preparation is an additional hypothesis of the loss model; its preparation time is outside $`T`$. Exact closed layers leave no residual displacement to reset, while the emitted bath record remains. Implementing or tracking local corrections likewise has device-dependent timing and errors outside the force fluence.

The collective excursion bound (H8), summed over modes at full filling $`K=4mL`$, gives $`\max_{z,t}\sum_\ell|\beta_{\ell,z}(t)|^2\le64mL=16K`$. Thus the construction allows occupation to grow. Neither the coefficient-force budget nor the exposure trace ensures a constant maximum-branch occupation.

A specified memory model makes another duration price explicit. If each of the $`2K`$ qubits has independent Poisson $`Z`$ errors at rate $`\gamma`$, its idle-only entanglement infidelity over duration $`T`$ is exactly

```math
1-F_e^{\rm idle}
=1-\left(\frac{1+e^{-2\gamma T}}2\right)^{2K}
=2K\gamma T+O((K\gamma T)^2).
\qquad\text{(H16)}
```

At fixed finite system size and weak noise, independent bus loss adds first-order coefficient $`\kappa X`$, so the leading infidelity is $`\kappa X+2K\gamma T`$. This is a perturbative fidelity metric in a specified noise model; it does not replace the nonperturbative global diamond bounds.

For the lossless individual-cap circular family, multiplying every harmonic by an integer $`q\ge1`$ preserves area but changes $`T`$ to $`T_1\sqrt q`$ and $`X`$ to $`X_1/\sqrt q`$. The leading expression becomes

```math
\frac{\kappa X_1}{\sqrt q}+2K\gamma T_1\sqrt q.
\qquad\text{(H17)}
```

For $`\gamma>0`$, its continuous optimum is $`q=\kappa X_1/(2K\gamma T_1)`$, clipped to $`q\ge1`$ before comparing adjacent integers. If $`\gamma=0`$ and $`\kappa>0`$, this unrestricted family has no finite minimizing winding. This optimizes only the first-order expression within this family. Damping compensation, modulation, and occupation still need checking. The small-excursion/more-winding idea is established in [Müller, Luoma and Strunz, Section III.2](https://arxiv.org/html/1907.08033v2); these formulas state its force and duration price.
