# Linear displacement-bus model and resource conventions

The results in this project concern a specified control model: commuting data Pauli operators drive linear displacements of a finite collection of harmonic oscillators. They are not bounds on unrestricted quantum architectures. The constructive optima assume independently programmable complex forces on every data–bus coupling. A device with fewer control channels is a restricted subclass: the converse still applies, but attainment need not.

Geometric phases from conditional oscillator trajectories, and their modification by dissipation, are established ingredients. See [Louis, Munro, Spiller and Nemoto, *Loss in hybrid qubit-bus couplings and gates*](https://arxiv.org/pdf/0804.3240) and [Müller, Luoma and Strunz, *Geometric phase gates in dissipative quantum dynamics*](https://arxiv.org/html/1907.08033v2). This page fixes the conventions needed for the resource statements. The exact noisy channel and the optimization over closed trajectories are derived in [loss_and_frontier.md](loss_and_frontier.md).

## 1. Dynamics and admissible controls

There are $`n`$ data qubits with commuting operators $`Z_i`$, and $`b\geq1`$ independent bosonic modes with $`[a_\mu,a_\nu^\dagger]=\delta_{\mu\nu}`$. In an interaction picture for the known free oscillator motion, set $`\hbar=1`$ and use

**(M1)**

```math
H(t)=i\sum_{\mu=1}^b\sum_{i=1}^n
 Z_i\bigl[u_{\mu i}(t)a_\mu^\dagger-u_{\mu i}(t)^*a_\mu\bigr].
```

Each $`u_{\mu i}\in L^2(0,T;\mathbb{C})`$ is available independently. In particular, its two quadratures are independently controllable; this is stronger than a single real laboratory force with a prescribed rotating phase. There is no direct two-qubit Hamiltonian available for free.

For the loss results, all buses and their input fields start in vacuum and the joint data–bus state obeys

**(M2)**

```math
\dot\rho=-i[H(t),\rho]
 +\kappa\sum_{\mu=1}^b
 \left(a_\mu\rho a_\mu^\dagger
 -\tfrac12\{a_\mu^\dagger a_\mu,\rho\}\right),
\qquad \kappa\geq0.
```

Thus $`\kappa`$ is the number-decay rate, and the coherent amplitude decays at rate $`\kappa/2`$. This convention is fixed by (M2), independently of rate notation used in other papers. Loss is Markovian, unmonitored, and has the same rate in all modes.

During the gate interval, the data coupling axis remains $`Z_i`$. No measurements, feedforward, intermediate noncommuting data rotations, auxiliary data encodings, squeezing, parametric amplification, nonlinear mediator control, or controlled bus mixing are included. Global phases and local diagonal $`Z`$ corrections may be ignored when specifying the target data gate. Statements about more general endpoint rotations require an additional equivalence argument; none is implicit in (M1).

## 2. Conditional trajectories, closure, and phase

Let $`A(t)\in\mathbb{C}^{b\times n}`$ have columns $`\alpha_i(t)`$, and write $`u(t)=(u_{\mu i}(t))`$. Define

**(M3)**

```math
\dot A(t)=u(t)-\frac\kappa2 A(t),\qquad A(0)=0.
```

For a computational string $`z\in\{+1,-1\}^n`$, the bus coherent amplitude is $`A(t)z`$. Since the sign strings span the real data-coordinate space, return to vacuum in every branch is equivalent to the matrix condition

**(M4)**

```math
A(T)=0.
```

We impose (M4) exactly. Equivalently, every coupling obeys

**(M5)**

```math
\int_0^T e^{\kappa t/2}u_{\mu i}(t)\,dt=0.
```

Conversely, any $`A\in H^1_0([0,T];\mathbb{C}^{b\times n})`$ is an admissible closed trajectory when driven by $`u=\dot A+\kappa A/2`$. The Sobolev condition gives continuous trajectories with well-defined endpoint values. It permits nonzero one-sided endpoint values of the force; a zero-force switching condition is an additional constraint.

Use the displacement convention $`D(\alpha)=\exp(\alpha a^\dagger-\alpha^*a)`$. A small drive displacement $`D(u\,dt)`$ acting on a coherent state of amplitude $`\alpha`$ contributes phase $`\mathrm{Im}(\alpha^*u)dt`$. Passive vacuum attenuation changes the coherent amplitudes without adding such a scalar phase. Therefore the accumulated phase in branch $`z`$ is

**(M6)**

```math
q_K(z)=\mathrm{Im}\int_0^T (A z)^\dagger u z\,dt
       =\mathrm{Im}\int_0^T (A z)^\dagger\dot A z\,dt
       =z^T Kz,
\quad
K=\mathrm{Im}\int_0^T A^\dagger\dot A\,dt.
```

The damping contribution $`\kappa\Vert Az\Vert ^2/2`$ is real and drops out of this expression. Integration by parts and closure give

```math
\left(\int_0^T A^\dagger\dot A\,dt\right)^\dagger
=-\int_0^T A^\dagger\dot A\,dt,
```

so $`K`$ is real symmetric. At zero loss the returned bus factors out and the data operation is

**(M7)**

```math
U_K=\exp\bigl(i\,\mathbf{Z}^T K\mathbf{Z}\bigr).
```

With loss, $`U_K`$ names the geometric part of the exact channel; it does not describe the whole operation.

The factor convention matters:

**(M8)**

```math
\mathbf{Z}^T K\mathbf{Z}
=\mathrm{tr}K+2\sum_{i\lt j}K_{ij}Z_iZ_j.
```

Thus the physical $`ZZ`$ angle is $`2K_{ij}`$, and a change of the ordinary matrix diagonal changes only the global gate phase. For a CZ edge, $`K_{ij}=\pi/8`$ is a representative. Allowing local $`Z`$ corrections gives the equivalent representatives $`K_{ij}=\pi/8+\pi N_{ij}/4`$, $`N_{ij}\in\mathbb{Z}`$. A missing edge has $`K_{ij}=\pi N_{ij}/4`$. One can check the necessity by taking the four-point mixed phase difference, which is $`8K_{ij}\bmod 2\pi`$; sufficiency follows because a $`\pi/4`$ shift of $`K_{ij}`$ multiplies the gate by $`iZ_iZ_j`$.

An optimum for a specified full matrix $`K`$ is consequently different from an optimum over all implementations of a quantum gate. Gate-level converses must allow every diagonal completion and every admissible phase representative.

## 3. What is paid

Define the real symmetric matrices

```math
F=\mathrm{Re}\int_0^T A^\dagger A\,dt,
\qquad
E_{\rm mat}=\mathrm{Re}\int_0^T\dot A^\dagger\dot A\,dt,
```

and the scalar resources

**(M9)**

```math
X=\mathrm{tr}F=\int_0^T\Vert A\Vert _F^2dt,
\quad
E=\mathrm{tr}E_{\rm mat}=\int_0^T\Vert \dot A\Vert _F^2dt,
\quad
G=\int_0^T\Vert u\Vert _F^2dt.
```

| Quantity | Meaning in this model | Units with dimensionless displacement |
|---|---|---|
| $`b`$ | Simultaneously available bosonic modes | Dimensionless |
| $`T`$ | Gate duration | Time |
| $`K`$ | Geometric phase matrix | Dimensionless |
| $`X`$ | Integrated displacement exposure | Time |
| $`E`$ | Squared trajectory-velocity integral | Inverse time |
| $`G`$ | Paid squared-force action | Inverse time |
| $`P`$ | Bound on instantaneous $`\sum_{\mu i}\lvert u_{\mu i}\rvert^2`$ | Inverse time squared |

We call $`G`$ the squared-force action. It is a quadratic control cost, not an assertion that a particular laboratory source expends $`G`$ joules. A hardware application must supply the conversion from its control amplitude to $`u`$.

Using (M3) and exact closure,

**(M10)**

```math
\begin{aligned}
G
&=E+\frac{\kappa^2}{4}X
  +\kappa\mathrm{Re}\int_0^T\mathrm{tr}(\dot A^\dagger A)\,dt\\
&=E+\frac{\kappa^2}{4}X.
\end{aligned}
```

In particular $`G=E`$ only at zero damping or for a trivial trajectory. Choosing a closed path under loss requires paying for the compensating force. A pointwise total-force cap implies $`G\leq PT`$; the reverse implication does not hold.

For a uniform random computational string, $`\mathbb{E}_z\Vert A(t)z\Vert ^2=\Vert A(t)\Vert _F^2`$. Thus $`X`$ is the basis-averaged integrated bus occupation, and $`\kappa X`$ is the corresponding average number of photons emitted into the vacuum output field. The coefficient cost $`\Vert u\Vert _F^2`$ likewise equals the basis average of the squared collective force $`\Vert uz\Vert ^2`$.

These are averages, not bounds on $`\max_z\Vert A(t)z\Vert ^2`$ or $`\max_z\Vert u(t)z\Vert ^2`$. Fixed bus occupation, Lamb–Dicke validity, per-qubit amplitude, slew-rate, and finite modulation bandwidth are additional resources. An infinite harmonic ladder is assumed. Finite-interval harmonic formulas with abrupt force switching are not strictly bandlimited waveforms.

## 4. Phase, exposure, and control inequalities

Closed trajectories obey the Gram and finite-time inequalities proved in [spectral_cost.md, §4](spectral_cost.md). In the notation above,

**(M11)**

```math
\begin{pmatrix}F&K\\K&E_{\rm mat}\end{pmatrix}\succeq0.
```

Consequently,

**(M12)**

```math
\ker F\subseteq\ker K,
\qquad KF^+K\preceq E_{\rm mat}.
```

Here $`F^+`$ is the Moore–Penrose inverse. There is also the scalar consequence

**(M13)**

```math
EX\geq\Vert K\Vert _*^2,
```

where $`\Vert K\Vert _*`$ is the sum of its eigenvalue magnitudes.

A stronger finite-time **trace** inequality is

**(M14)**

```math
E\geq\frac{\Vert K\Vert _*^2}{X}+\frac{\pi^2}{T^2}X,
\qquad X\gt 0.
```

Together with the paid-action identity (M10), this yields

**(M15)**

```math
G\geq\frac{\Vert K\Vert _*^2}{X}
 +\left(\frac{\pi^2}{T^2}+\frac{\kappa^2}{4}\right)X.
```

The finite-time term in (M14) is a trace statement; it cannot generally be added to (M12) as a matrix-order inequality. The proof and an explicit counterexample to that stronger claim are in [spectral_cost.md, §4](spectral_cost.md). The spectrum in [loss_and_frontier.md](loss_and_frontier.md) supplies the additional finite-bus multiplicity constraints missing from (M14).

## 5. Environmental rank is not physical bus count

The complex trajectory Gram matrix is

**(M16)**

```math
C=\int_0^T A^\dagger A\,dt=F+iJ,
\qquad J^T=-J.
```

For $`\kappa\gt 0`$, $`F`$ describes the real span of the emitted displacement records. The first part of (M12) implies $`\mathrm{rank}F\geq\mathrm{rank}K`$. But $`C`$ describes their complex span, and $`\mathrm{rank}F\leq2\mathrm{rank}C`$. For example, a single row $`A(t)=f(t)(1,1,i,i)`$, with a closed scalar path of nonzero area, has $`\mathrm{rank}C=1`$ and $`\mathrm{rank}F=\mathrm{rank}K=2`$.

Thus a rank statement about real environmental records cannot be identified with the number of complex jump operators or the number $`b`$ of physical bus modes. One bus can emit many temporal modes. The relevant obstruction is the control cost of supplying sufficiently many temporal directions, quantified by the spectrum derived in the companion page.
