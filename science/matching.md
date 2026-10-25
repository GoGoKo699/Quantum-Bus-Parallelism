# Parallel CZ matchings: phase lifts, finite costs, and accuracy

This page proves a gate-level congestion law for $`m`$ disjoint CZ gates mediated during one interval by $`b`$ complex linear bosonic buses. The converse includes every exact quadratic phase lift, all free diagonal completions, and arbitrary local $`Z`$ and global phases. It also applies at fixed nonzero accuracy, including directly to the implemented Markovian lossy channel under the assumptions below.

The conclusion is a lossless minimum coefficient-force energy of order

```math
\frac{m+m^2/b}{T}.
```

The exact finite-size optimum over all phase lifts is not computed in closed form. We prove explicit lower and constructive upper bounds with the same scaling. At nonzero loss the results here are necessary conditions, not a tight noisy-gate construction.

The weighted spectral control method is inherited from Wong–Baillieul and the Brockett/Rizzi–Serres matrix-area literature; see the primary references and self-contained proof in [spectral_cost.md](spectral_cost.md). The additional gate-level work is the minimization over quantum phase equivalence, its Boolean unwrapping at finite accuracy, and the physical distinction between total and individual coupling budgets.

## 1. Conventions and precise scope

Label the $`2m`$ spins by $`\mathcal{A}=\{A_1,\ldots,A_m\}`$ and $`\mathcal{B}=\{B_1,\ldots,B_m\}`$. The target is

```math
U_{\mathrm{CZ}}=\prod_{j=1}^m\mathrm{CZ}_{A_jB_j}.
```

Arbitrary diagonal one-spin phases and a global phase may dress the target. Write $`x_i=(1-z_i)/2`$, with $`x_i\in\{0,1\}`$ and $`z_i\in\{-1,1\}`$. Then

```math
U_{\mathrm{CZ}}\vert x\rangle
=e^{i\pi\sum_jx_{A_j}x_{B_j}}\vert x\rangle,
```

and each pair has $`Z_{A_j}Z_{B_j}`$ coefficient $`\pi/4`$ after local and global phases are removed.

Let $`A(t)\in\mathbb{C}^{b\times2m}`$ have entries in $`H_0^1(0,T)`$, and define

**(M.1)**

```math
K=\mathrm{Im}\int_0^TA^\dagger\dot A\,dt,
\qquad
E=\int_0^T\Vert \dot A\Vert _F^2dt.
```

All trajectories close exactly: $`A(0)=A(T)=0`$. The spin gate at zero loss is
$`U_K\vert z\rangle=e^{iz^{\mathsf{T}}Kz}\vert z\rangle`$, so its pair coefficient is $`2K_{ij}`$. Put

**(M.2)**

```math
c=\frac{\pi}{8},
\qquad
C=K_{\mathcal{A}\mathcal{B}},
\qquad
w_j=\left\lceil\frac{j}{4b}\right\rceil,
\qquad
S_{m,b}=\sum_{j=1}^m w_j.
```

We use the nuclear norm $`\Vert \cdot\Vert _*`$, Frobenius norm $`\Vert \cdot\Vert _F`$, and operator norm $`\Vert \cdot\Vert _{\mathrm{op}}`$ with their usual matrix meanings. All channel error statements use the **half-diamond distance**
$`d_\diamond(\mathcal{E},\mathcal{V})=\tfrac12\Vert \mathcal{E}-\mathcal{V}\Vert _\diamond`$.

The model permits arbitrary complex coefficient forces while the coupled spin observables commute. It imposes no finite boson occupation cutoff, maximum computational-branch displacement, hard bandwidth, or finite slew bound. Noncommuting control between force segments, extra spin ancillas, measurement and feedback, squeezing, nonlinear buses, and uncharged bus mixing lie outside the theorem.

## 2. Every exact phase lift

**Lemma M1 (complete exact lift class).** The gate $`U_K`$ equals the target matching up to local $`Z`$ and global phases if and only if, for every $`i\lt j`$,

**(M.3)**

```math
K_{ij}=\frac{\pi}{8}\Gamma_{ij}+\frac{\pi}{4}N_{ij},
\qquad N_{ij}\in\mathbb{Z},
```

where $`\Gamma`$ is the matching adjacency matrix. The diagonal of $`K`$ is arbitrary. In particular,

**(M.4)**

```math
\boxed{C=c(I_m+2B),\qquad B\in\mathbb{Z}^{m\times m}.}
```

There is no small-phase or principal-branch restriction on $`B`$.

**Proof.** The coefficient of $`x_ix_j`$ in $`z^{\mathsf{T}}Kz`$ is $`8K_{ij}`$. Taking the mixed four-point phase difference in $`x_i,x_j`$ cancels every constant and one-spin phase. Equality of diagonal unitaries therefore requires
$`8K_{ij}-\pi\Gamma_{ij}\in2\pi\mathbb{Z}`$, proving necessity.

Conversely, increasing an off-diagonal $`K_{ij}`$ by $`\pi N/4`$ multiplies the gate by

```math
e^{i(\pi N/2)Z_iZ_j}
=i^N Z_i^N Z_j^N.
```

This is a product of one-spin $`Z`$ operators and a scalar. Such factors commute, so all the integers in (M.3) are independently allowed. Diagonal changes contribute only a scalar. This proves sufficiency. $`\square`$

The full lift class also requires all same-side off-diagonal entries to be multiples of $`\pi/4`$. The lower bounds below discard those extra restrictions and therefore remain valid. An arbitrary spectral completion of a general cross block need not satisfy them; that distinction is respected in the upper construction.

### Optional exact endpoint-local observation

The exact statement does not become weaker if arbitrary one-qubit unitaries, rather than only $`Z`$ phases, are allowed before and after the bus interval. If a diagonal $`D`$ is related to the matching by such product unitaries, then $`D`$ factors over the same disjoint pairs. Since all its diagonal entries are nonzero and all off-diagonal entries vanish, each two-qubit tensor factor is itself diagonal up to a scalar. A diagonal two-qubit gate can be written, up to local diagonal phases, as $`e^{i\gamma Z\otimes Z}`$. Its two operator-Schmidt coefficients are $`2\vert \cos\gamma\vert `$ and $`2\vert \sin\gamma\vert `$. Local equivalence to CZ makes both equal to $`\sqrt2`$, forcing $`\gamma=\pi/4\pmod{\pi/2}`$. Hence (M.3) still follows.

The finite-error theorem below keeps the stated diagonal-target scope. It does not assume a stability theorem for arbitrary non-diagonal endpoint rotations.

## 3. Exact matching cost, including all lifts

Let $`E^*_{m,b}(T)`$ be the minimum energy of a lossless exact implementation, with all lifts and local/global phases allowed. The fixed-matrix theorem gives the exact variational characterization

**(M.5)**

```math
E^*_{m,b}(T)
=\frac{2\pi}{T}\min_{K\in\mathfrak{K}_m}\Phi_b(K),
```

where $`\mathfrak{K}_m`$ is the class (M.3), including arbitrary real diagonals. This is a genuine minimum: $`\mathfrak{K}_m`$ is closed, $`\Phi_b`$ is continuous, and
$`\Phi_b(K)\geq\Vert K\Vert _*`$ makes its sublevel sets bounded. Formula (M.5) should not be confused with a solved closed-form integer optimization.

**Theorem M2 (finite exact sandwich).** For every $`m,b\geq1`$ and $`T\gt 0`$,

**(M.6)**

```math
\boxed{
\frac{\pi^2}{2T}\,
m\left(\prod_{j=1}^m w_j\right)^{1/m}
\ \leq\
E^*_{m,b}(T)
\ \leq\
\frac{\pi^2}{2T}S_{m,b}.
}
```

In particular,

**(M.7)**

```math
E^*_{m,b}(T)\geq
\frac{\pi^2}{2T}
\max\left\{
m,\,
\frac{m(m!)^{1/m}}{4b}
\right\}.
```

The upper bound has a closed expression. If $`m=4bq+r`$, with integers $`q\geq0`$ and $`0\leq r\lt 4b`$, then

**(M.8)**

```math
S_{m,b}=2bq(q+1)+(q+1)r.
```

When $`m\leq4b`$, every $`w_j=1`$, so the lower and upper bounds coincide:
$`E^*_{m,b}(T)=\pi^2m/(2T)`$. This is an exact optimum over all lifts in that regime. For larger matchings, (M.6) remains a sandwich rather than a closed-form solution of the lift optimization.

### 3.1. Proof of the converse

For every allowed lift, $`I_m+2B`$ is the identity over $`\mathbb{F}_2`$. Its determinant is an odd integer, in particular nonzero. Thus

**(M.9)**

```math
\prod_{j=1}^m\sigma_j(C)
=\vert \det C\vert 
\geq c^m.
```

The sharp cross-block theorem, Theorem SC2, gives

```math
E\geq\frac{4\pi}{T}\sum_{j=1}^m w_j\sigma_j(C).
```

Arithmetic–geometric mean, applied to the positive numbers $`w_j\sigma_j(C)`$, yields

```math
\sum_jw_j\sigma_j(C)
\geq m\left(\prod_jw_j\,\prod_j\sigma_j(C)\right)^{1/m}
\geq cm\left(\prod_jw_j\right)^{1/m}.
```

This proves the lower bound in (M.6) without choosing a phase branch or diagonal completion. Since $`w_j\geq1`$ and $`w_j\geq j/(4b)`$, it also proves (M.7). The factor $`\pi/8`$ in $`c`$ follows from the physical pair coefficient $`2K_{ij}`$; replacing it by $`\pi/4`$ would double the claimed lower bound incorrectly.

### 3.2. Explicit lossless upper construction

Take the unlifted cross block $`C=cI_m`$. Assign pair $`j`$ to
$`k_j=w_j`$. At every harmonic magnitude $`k`$, allocate up to $`2b`$ pairs to sign $`s_j=+1`$ and up to $`2b`$ to sign $`s_j=-1`$. Within each sign, assign each pair a distinct bus/quadrature slot
$`(\mu_j,\chi_j)`$, where $`\mu_j\in\{1,\ldots,b\}`$ and $`\chi_j\in\{1,i\}`$. Each harmonic magnitude therefore carries $`4b`$ pairs.

Put

```math
a_k=\sqrt{\frac{c}{2\pi k}},
\qquad
\omega_k=\frac{2\pi k}{T}.
```

The only nonzero coefficients for pair $`j`$ are

**(M.10)**

```math
\begin{aligned}
\alpha_{\mu_j,A_j}(t)
&=\chi_j a_{k_j}(e^{is_j\omega_{k_j}t}-1),\\
\alpha_{\mu_j,B_j}(t)
&=s_j\chi_j a_{k_j}(e^{is_j\omega_{k_j}t}-1).
\end{aligned}
```

The resulting pair block is

**(M.11)**

```math
\begin{pmatrix}
K_{A_jA_j}&K_{A_jB_j}\\
K_{B_jA_j}&K_{B_jB_j}
\end{pmatrix}
=
\begin{pmatrix}
s_jc&c\\c&s_jc
\end{pmatrix}.
```

Different buses have zero cross terms. The two quadrature slots at one signed harmonic have zero real Gram cross term. Different signed harmonics have zero area cross term by Fourier orthogonality. The subtracted constants contribute no area. Thus there are no unintended same-side or cross-pair interactions.

Every trajectory closes. The diagonal terms in (M.11) are global phases, and a final local diagonal correction gives the literal CZ target. Each qubit has constant coefficient-force power

**(M.12)**

```math
\sum_\mu\vert u_{\mu,A_j}(t)\vert ^2
=\sum_\mu\vert u_{\mu,B_j}(t)\vert ^2
=\frac{\pi^2k_j}{4T^2},
\qquad u=\dot A.
```

Summing the two qubits of every pair proves

**(M.13)**

```math
\sum_{\mu,i}\vert u_{\mu i}(t)\vert ^2
=\frac{\pi^2}{2T^2}S_{m,b},
\qquad
E=\frac{\pi^2}{2T}S_{m,b},
```

which establishes the upper bound in (M.6). Total coefficient-force power is constant throughout the interval; there is no additional peak-total-power factor.

This construction is exact for the unlifted cross block with its allowed diagonal completion. We do not claim that no other integer lift improves its finite-size energy.

## 4. Scaling and the two power conventions

The elementary bounds

**(M.14)**

```math
(m!)^{1/m}\geq m/e,
\qquad
S_{m,b}\leq m+\frac{m(m-1)}{8b}
```

show that, with constants independent of $`m,b,T`$,

**(M.15)**

```math
E^*_{m,b}(T)=
\Theta\!\left(\frac{m+m^2/b}{T}\right).
```

For example, a fully explicit, though nonoptimal, all-size sandwich is

**(M.16)**

```math
\frac{\pi^2}{2(1+4e)T}\left(m+\frac{m^2}{b}\right)
\leq E^*_{m,b}(T)
\leq
\frac{\pi^2}{2T}\left(m+\frac{m^2}{8b}\right).
```

The first inequality follows from
$`\max\{1,x/(4e)\}\geq(1+x)/(1+4e)`$ with $`x=m/b`$.

### 4.1. Instantaneous total coefficient-force cap

If

**(M.17)**

```math
\sum_{\mu,i}\vert u_{\mu i}(t)\vert ^2\leq P
\quad\text{for almost every }t,
```

then $`E\leq PT`$. Every exact lossless implementation satisfies

**(M.18)**

```math
T^2\geq
\frac{\pi^2}{2P}
m\left(\prod_jw_j\right)^{1/m}
\geq
\frac{\pi^2}{8bP}m(m!)^{1/m}.
```

Conversely, the construction (M.10) respects (M.17) whenever

**(M.19)**

```math
T^2\geq\frac{\pi^2}{2P}S_{m,b}.
```

Thus the lossless optimal duration under this resource scales as
$`\Theta(\sqrt{(m+m^2/b)/P})`$.
If one writes $`P=mp`$, then $`p`$ is a **per-pair total budget**. It must not simultaneously be called a per-qubit budget.

### 4.2. Individual qubit coefficient-force cap

Suppose instead that each physical qubit obeys

**(M.20)**

```math
\sum_\mu\vert u_{\mu i}(t)\vert ^2\leq g^2.
```

This implies the total cap $`P=2mg^2`$, so (M.7) gives

**(M.21)**

```math
T^2\geq\frac{\pi^2}{4g^2}
\max\left\{1,\frac{(m!)^{1/m}}{4b}\right\}.
```

Equation (M.12) supplies a distinct constructive upper bound:

**(M.22)**

```math
T=\frac{\pi}{2g}
\sqrt{\left\lceil\frac{m}{4b}\right\rceil}
\quad\text{is sufficient at zero loss}.
```

Hence the lossless duration is
$`\Theta(g^{-1}\sqrt{1+m/b})`$ under the individual caps as well. Its finite constants differ from those obtained using only a total cap, because the harmonic construction allocates different powers to different pairs.

The highest modulation frequency within the interval is
$`2\pi\lceil m/(4b)\rceil/T`$. The forces in (M.10) do not vanish at the interval endpoints, so turning them on and off produces spectral tails. These formulas impose no strict Fourier bandwidth or slew bound.

Neither (M.17) nor (M.20) bounds $`\max_z\Vert u(t)z\Vert ^2`$ or $`\max_z\Vert A(t)z\Vert ^2`$. A worst-case branch can coherently add many coefficients on a common bus. The construction may therefore require large transient boson occupation; a finite-occupation architecture needs an additional analysis.

## 5. Uniform phase unwrapping on the Boolean cube

**Lemma M3 (integer quadratic unwrapping).** Let $`q:\{0,1\}^n\to\mathbb{R}`$ be represented by a real multilinear polynomial of degree at most two. Suppose

**(M.23)**

```math
q(x)=2\pi h(x)+e(x),
\qquad
h(x)\in\mathbb{Z},
\qquad
\vert e(x)\vert \leq\delta\lt \frac{\pi}{4}
```

at every Boolean string. Then the unique multilinear representation of $`h`$ has degree at most two and has integer coefficients. In particular, $`e`$ is itself a quadratic polynomial on the cube.

**Proof.** On every three-coordinate subcube, with all other coordinates fixed, the mixed third difference satisfies $`D_iD_jD_kq=0`$. Therefore

```math
2\pi\vert D_iD_jD_kh\vert 
=\vert D_iD_jD_ke\vert 
\leq8\delta\lt 2\pi.
```

The third difference of $`h`$ is an integer and must vanish. All higher mixed differences then vanish as well. Equivalently, every coefficient of degree at least three in the unique multilinear expansion is zero. Each remaining coefficient is a finite difference of integer values of $`h`$ at the origin, so it is integer. For $`n\lt 3`$, the degree assertion is automatic and the same integer-coefficient argument applies. $`\square`$

The strict $`\delta\lt \pi/4`$ assumption is used at the integer step. No bound on the size or number of the wraps $`h(x)`$ is needed.

### 5.1. Consequence for the phase matrix

Apply the lemma to the difference between the bus phase and the matching target phase, permitting any added constant and one-spin polynomial. In the $`z`$ variables, the coefficient of $`z_iz_j`$ in $`2\pi h`$ is an integer multiple of $`\pi/2`$. Therefore

**(M.24)**

```math
\boxed{
C=c(I_m+2B)+R,\qquad
B\in\mathbb{Z}^{m\times m},\qquad
\Vert R\Vert _F\leq\delta/2.
}
```

For the final inequality, expand the bounded residual $`e(z)`$ in the orthonormal Walsh characters on the uniform sign cube. Its pair coefficient is $`2R_{ij}`$, where $`R_{ij}`$ denotes the corresponding entry of the full phase-matrix residual. Parseval gives

**(M.25)**

```math
4\sum_{i\lt j}R_{ij}^2
\leq\mathbb{E}_z[e(z)^2]\leq\delta^2.
```

The rectangular cross-block Frobenius norm counts each cross pair once, so $`\Vert R_{\mathcal{A}\mathcal{B}}\Vert _F\leq\delta/2`$. There is no factor $`\sqrt2`$ here; that factor would arise only if one counted both symmetric copies in the full matrix norm.

### 5.2. From unitary-channel error to a phase arc

Suppose $`U_K`$ and a diagonally dressed matching target $`V`$ have
$`d_\diamond(\mathcal{U}_K,\mathcal{V})\leq\epsilon\lt 1`$.
For two unitary channels, their half-diamond distance equals
$`\sqrt{1-\nu^2}`$, where $`\nu`$ is the distance of the convex hull of the eigenvalues of $`V^\dagger U_K`$ from zero. One way to see the formula is to optimize the trace distance of the two pure outputs: their overlap is $`\mathrm{tr}(\rho V^\dagger U_K)`$, with arbitrary input density matrix $`\rho`$, including the reduced state of an ancilla-assisted pure input.

Since $`\epsilon\lt 1`$, this convex hull excludes zero and the eigenvalues lie in an open semicircle. If their shortest containing arc has width $`\Delta\lt \pi`$, its chord gives $`\nu=\cos(\Delta/2)`$, hence $`\Delta\leq2\arcsin\epsilon`$. Choosing the midpoint of that arc as the global phase gives (M.23) with

**(M.26)**

```math
\delta=\arcsin\epsilon.
```

Thus (M.24) follows whenever $`\epsilon\lt 1/\sqrt2`$. Local diagonal phases merely change the constant and linear coefficients of $`q`$.

## 6. Explicit finite-error lower bounds, positive for every $`m`$

Assume (M.24), and define

**(M.27)**

```math
\eta=\frac{4\delta}{\pi}\in[0,1),
\qquad
Q_m=\sum_{j=1}^mj^2=\frac{m(m+1)(2m+1)}6.
```

**Theorem M4 (all-size robust congestion).** Every such closed trajectory satisfies

**(M.28)**

```math
\boxed{
E\geq\frac{\pi^2}{2T}
\max\left\{
m-\eta\sqrt m,\,
\frac{m(m!)^{1/m}-\eta\sqrt{Q_m}}{4b}
\right\}.
}
```

The first term is strictly positive for every $`m\geq1`$. A sharper additional lower bound is

**(M.29)**

```math
E\geq\frac{\pi^2}{2T}
\left[
m\left(\prod_jw_j\right)^{1/m}
-\eta\left(\sum_jw_j^2\right)^{1/2}
\right].
```

The bracket in (M.29), or the second term in (M.28), can be negative at small sizes and large allowed error. They are to be combined with the positive first term in (M.28), not presented as standalone positive constants.

For an elementary bound with no size threshold in its statement,

**(M.30)**

```math
\boxed{
E\geq
\frac{\pi^2(1-\eta)}{60T}
\left(m+\frac{m^2}{b}\right)
\qquad\text{for all integers }m,b\geq1.
}
```

The numerical constant $`1/60`$ is deliberately conservative. Equations (M.28)–(M.29) retain better finite-size information.

### 6.1. Proof of the perturbation estimates

Put $`C_0=c(I+2B)`$. Its determinant remains odd after removing the factor $`c^m`$, so

**(M.31)**

```math
\Vert C_0\Vert _*\geq cm,
\qquad
\sum_jj\,\sigma_j(C_0)\geq cm(m!)^{1/m}.
```

The singular-value perturbation inequality in Frobenius norm gives

**(M.32)**

```math
\left(\sum_j[\sigma_j(C)-\sigma_j(C_0)]^2\right)^{1/2}
\leq\Vert C-C_0\Vert _F\leq\delta/2.
```

Consequently

**(M.33)**

```math
\begin{aligned}
\Vert C\Vert _*&\geq cm-\frac{\delta}{2}\sqrt m,\\
\sum_jj\,\sigma_j(C)
&\geq cm(m!)^{1/m}-\frac{\delta}{2}\sqrt{Q_m}.
\end{aligned}
```

Combining these with $`E\geq(4\pi/T)\Vert C\Vert _*`$ and
$`E\geq(\pi/(bT))\sum_jj\,\sigma_j(C)`$ proves (M.28).
The same Cauchy–Schwarz estimate with the weights $`w_j`$, together with weighted arithmetic–geometric mean, proves (M.29).

The weighted function $`\sum_jw_j\sigma_j(C)`$ is not being assumed to be a norm or to satisfy a triangle inequality. Equation (M.32), applied to the ordered singular-value vectors, is the actual stability argument.

### 6.2. Proof of the positive all-size constant

The first term in the maximum in (M.28) is at least $`(1-\eta)m`$. Also,
$`(m!)^{1/m}\geq m/e`$ and $`\sqrt{Q_m}\leq m^{3/2}`$. For $`m\geq30\gt 4e^2`$,

```math
\frac{m(m!)^{1/m}-\eta\sqrt{Q_m}}{4b}
\geq\frac{m^2}{8eb}.
```

With $`a=1-\eta\gt 0`$, elementary optimization in $`m/b`$ gives

```math
\max\left\{am,\frac{m^2}{8eb}\right\}
\geq\frac{a}{1+8ea}
\left(m+\frac{m^2}{b}\right)
\geq\frac a{30}\left(m+\frac{m^2}{b}\right).
```

For $`m\leq29`$, use $`b\geq1`$ to obtain
$`m+m^2/b\leq30m`$, and the first term alone proves the same bound. Multiplying by $`\pi^2/(2T)`$ proves (M.30). The number $`30`$ is only a convenient proof threshold; the theorem and (M.28) apply from $`m=1`$.

For fixed accuracy with $`\eta\lt 1`$, the exact zero-loss construction remains admissible for an approximate target. Thus the lossless approximate optimum has the same
$`\Theta_\epsilon((m+m^2/b)/T)`$ energy scaling, even with arbitrary phase wraps.

Under an instantaneous total coefficient-force cap $`P`$, (M.30) implies

**(M.34)**

```math
T\geq
\sqrt{\frac{\pi^2(1-\eta)}{60P}
\left(m+\frac{m^2}{b}\right)}.
```

Under the individual caps (M.20), it implies

**(M.35)**

```math
T\geq\frac{\pi}{\sqrt{120}\,g}
\sqrt{(1-\eta)\left(1+\frac mb\right)}.
```

The sharper bounds follow directly by substituting (M.28) instead of (M.30).

## 7. Direct robustness for the implemented lossy channel

The preceding argument also applies directly to the actual spin channel in a specified noisy physical model. Assume vacuum initial buses, vacuum Markov input fields, common loss rate $`\kappa\geq0`$, linear commuting spin-dependent forces, and exactly closed **damped** trajectories

**(M.36)**

```math
\dot A=u-\frac{\kappa}{2}A,
\qquad A(0)=A(T)=0.
```

Define

**(M.37)**

```math
F+iJ=\int_0^TA^\dagger A\,dt.
```

Here $`F`$ is real symmetric and $`J`$ is real antisymmetric. In a computational branch $`z`$, the output field has coherent amplitude $`\sqrt\kappa\,A(t)z`$ and the scalar spin phase is $`z^{\mathsf{T}}Kz`$. Taking the coherent-state overlap with branch $`r`$ gives the Schur multiplier

**(M.38)**

```math
\lambda_{zr}
=
\exp\!\left[-\frac{\kappa}{2}(z-r)^{\mathsf{T}}F(z-r)\right]
\exp i\!\left[
z^{\mathsf{T}}Kz-r^{\mathsf{T}}Kr+\kappa r^{\mathsf{T}}Jz
\right].
```

This fixes the sign convention for $`J`$ by $`F+iJ=\int A^\dagger A`$. In particular, the bath phase is generally not the difference of two scalar diagonal-unitary phases. It cannot simply be deleted from the channel.

**Theorem M5 (noisy phase extraction).** If the actual channel (M.38) has half-diamond distance at most

**(M.39)**

```math
\epsilon\lt \frac1{2\sqrt2}
```

from a diagonally dressed matching target, then (M.24) and all the lower bounds (M.28)–(M.30) hold with

**(M.40)**

```math
\delta=\arcsin(2\epsilon),
\qquad
\eta=\frac4\pi\arcsin(2\epsilon).
```

No premise that the ideal area gate $`U_K`$ is itself close to the target is required.

**Proof.** Fix one computational reference string $`r`$ once and for all. For each $`z\ne r`$, input
$`(\vert z\rangle+\vert r\rangle)/\sqrt2`$. If $`v_zv_r^*`$ is the target coherence multiplier, the difference of the two output states has off-diagonal entries
$`(\lambda_{zr}-v_zv_r^*)/2`$ and its conjugate. Its half-trace norm is
$`\vert \lambda_{zr}-v_zv_r^*\vert /2`$. Therefore

**(M.41)**

```math
\vert \lambda_{zr}-v_zv_r^*\vert \leq2\epsilon.
```

After dividing by the target phase, write the actual multiplier as $`a e^{i\phi}`$, with $`0\leq a\leq1`$. The disk
$`\vert a e^{i\phi}-1\vert \leq2\epsilon\lt 1`$ excludes zero. Its largest angular deviation from the positive real axis is the tangent-ray angle $`\arcsin(2\epsilon)`$, so

**(M.42)**

```math
\vert \phi\bmod2\pi\vert \leq\delta.
```

With $`r`$ fixed, the term $`\kappa r^{\mathsf{T}}Jz`$ is linear in $`z`$. Consequently the phase difference in (M.42), including the target phase and the fixed reference phase, is a degree-at-most-two Boolean polynomial. Its quadratic coefficients are exactly the differences of the geometric $`K`$ and the matching target. The bath term changes only the linear coefficients. Apply Lemma M3, since (M.39) makes $`\delta\lt \pi/4`$, and then apply Parseval as in (M.25). This proves (M.24) and the claimed bounds. $`\square`$

The reference-dependent linear term is an algebraic device in the proof. The argument does not assert that one physical local correction removes the skew bath phase for every pair of computational branches simultaneously.

### 7.1. Which energy is paid in the damped device?

For closed trajectories, the physical coefficient-drive energy is exactly

**(M.43)**

```math
G=\int_0^T\Vert u\Vert _F^2dt
=E+\frac{\kappa^2}{4}X,
\qquad
X=\mathrm{tr}F.
```

The integrated cross term vanishes because
$`\mathrm{Re}\int\mathrm{tr}(\dot A^\dagger A)dt =\tfrac12[\Vert A(T)\Vert _F^2-\Vert A(0)\Vert _F^2]=0`$.
Thus $`G\geq E`$, and the bounds proved here apply to $`G`$ as well.
If the instantaneous physical drives obey $`\sum_{\mu,i}\vert u_{\mu i}(t)\vert ^2\leq P`$, then $`G\leq PT`$, so the timing converse (M.34) also applies directly to the noisy implementation with (M.40).

This is a necessary congestion bound. It does not supply a noisy construction meeting the requested $`\epsilon`$, an optimal diamond-error frontier, or a fault-tolerance threshold. The closed-loop condition remains exact throughout; allowing residual bus entanglement or approximate bus return requires a separate argument.

## 8. Proof status and boundaries

The fixed-$`K`$ spectral minimum, sharp cross-block bound, complete exact lift class, finite exact sandwich, explicit total and individual lossless constructions, Boolean unwrapping, and finite-error lower bounds above have analytic proofs. The noisy extension uses the explicit linear vacuum Markov dilation (M.38), including its antisymmetric bath-Gram phase.

The principal limitations are concrete:

- The optimum for a specified $`K`$ is exact; the optimum over all gate-equivalent integer lifts is bounded, not evaluated in closed form.
- Exact and approximate gate theorems use the same local $`Z`$/global dressing convention. The optional exact endpoint-local observation does not enlarge the finite-error theorem.
- Arbitrary waveform access is assumed for the upper construction. Addressing restrictions may worsen its attainable cost.
- Coupling-coefficient power, computational-branch force, photon occupation, and modulation bandwidth are different resources. Only the first is budgeted here.
- The exact lossless construction proves tight congestion scaling. No matching noisy upper bound is claimed.
- Interspersed noncommuting spin controls, active Gaussian resources, nonlinear or encoded buses, and approximate loop closure require new models and proofs.

## Mathematical provenance

The spectral input is credited to the existing bilinear-control and matrix-area program: W. S. Wong and J. Baillieul, [*Control Communication Complexity of Distributed Actions*](https://arxiv.org/abs/1201.6527v2), Theorem 5.1 and Corollary 5.1; R. W. Brockett, [*Control Theory and Singular Riemannian Geometry*](https://hrl.harvard.edu/publications/brockett81control.pdf), Theorem 2; and L. Rizzi and U. Serres, [*On the cut locus of free, step two Carnot groups*](https://arxiv.org/html/1610.01596v2), Appendix A, Proposition 15. The present page uses the symmetric, $`b`$-bus normalization established in Theorems SC1–SC2 and supplies the separate quantum phase-equivalence and robustness argument.
