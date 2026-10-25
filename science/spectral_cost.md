# Exact spectral cost of closed conditional displacements

For commuting forces through $`m`$ harmonic modes, the least fluence needed to generate a prescribed real phase matrix is an integer-weighted sum of its positive and negative eigenvalues. The weights count how many independent real directions fit at each Fourier harmonic. This section proves the exact result for square-integrable complex forces, including infinite Fourier series, and gives controls that attain it.

The weighted spectral method belongs to the bilinear-control and spectral area-minimization tradition of [Wong–Baillieul, Theorem 5.1 and Corollary 5.1](https://arxiv.org/pdf/1201.6527v2), [Brockett](https://hrl.harvard.edu/publications/brockett81control.pdf) and [Rizzi–Serres](https://doi.org/10.1090/proc/13658). The connection to that work is made explicit below. The further optimization over physically equivalent gates is a separate step, developed in [gate-layer bounds](gate_layer_bounds.md). Section 6 gives the sharp cross-block form used there; Section 7 connects phase to displacement exposure.

## 1. Control class and normalization

Use the Hamiltonian and interaction picture of the [model](model.md), allowing any number $`n\ge1`$ of qubits:

```math
\frac{H(t)}{\hbar}
=i\sum_{j=1}^{n}\sum_{\ell=1}^{m}
Z_j\bigl[u_{j\ell}(t)a_\ell^\dagger-u_{j\ell}(t)^*a_\ell\bigr],
\qquad m\ge1,\quad T>0.
\qquad\text{(1)}
```

For each mode, collect the forces and displacements into vectors $`u_\ell,\alpha_\ell\in\mathbb C^n`$. The admissible forces satisfy

```math
u_\ell\in L^2([0,T];\mathbb C^n),\qquad
\alpha_\ell(t)=\int_0^t u_\ell(s)\,ds,\qquad
\alpha_\ell(0)=\alpha_\ell(T)=0.
\qquad\text{(2)}
```

Equivalently, $`\alpha_\ell`$ is an $`H^1`$ path with zero endpoint values. In one time dimension an $`H^1`$ path has an absolutely continuous representative, so these endpoint conditions and the integrals below are well defined. Closure is imposed for every qubit and every mode; the final displacement then vanishes for every computational-basis configuration, returning the bus in the interaction picture for any initial bus state.

The spin propagator and fluence are

```math
U_A=\exp(iZ^{\mathsf T}AZ),\qquad
A_{ij}=\mathrm{Im}\sum_{\ell=1}^{m}
\int_0^T\alpha_{i\ell}(t)^*\dot\alpha_{j\ell}(t)\,dt,
\qquad
\mathcal E=\int_0^T\sum_{\ell=1}^{m}\lVert u_\ell(t)\rVert^2\,dt.
\qquad\text{(3)}
```

Integration by parts gives

```math
\int_0^T\alpha_{i\ell}^*\dot\alpha_{j\ell}\,dt
=-\left(\int_0^T\alpha_{j\ell}^*\dot\alpha_{i\ell}\,dt\right)^*,
\qquad\text{(4)}
```

so $`A`$ is real symmetric. In particular, the coefficient of $`Z_iZ_j`$ for $`i<j`$ is $`2A_{ij}`$, while $`\mathrm{tr}A`$ contributes only a global phase. The matrix $`A`$ and the action $`T\mathcal E`$ are dimensionless; $`\mathcal E`$ is the fluence of the effective Hamiltonian forces, with units of inverse time.

For smooth controls, (3) follows directly from the Weyl displacement composition law. The same formula holds for (2): approximate the zero-mean $`L^2`$ forces by zero-mean Fourier polynomials. Their primitives converge uniformly, their phase integrals converge, and Weyl displacements are strongly continuous in their amplitudes. At closure the propagators are finite-dimensional spin unitaries tensored with the bus identity, so their endpoint convergence is also in operator norm. This gives an extension to the stated control class without relying on a formal manipulation of unbounded oscillator operators.

## 2. Exact minimum for a prescribed full matrix

For $`A\in\mathrm{Sym}_n(\mathbb R)`$, let $`\lambda_r^+(A)`$ be its positive eigenvalues in nonincreasing order and let $`\lambda_r^-(A)`$ be the magnitudes of its negative eigenvalues in nonincreasing order. Append zeros to each list. Define

```math
\Phi_m(A)=\sum_{r=1}^{n}
\left\lceil\frac r{2m}\right\rceil
\bigl[\lambda_r^+(A)+\lambda_r^-(A)\bigr].
\qquad\text{(5)}
```

**Theorem 1 — spectral fluence.** For fixed $`T>0`$ and $`m\ge1`$, the minimum of (3) over all controls (2) producing a prescribed full real symmetric matrix $`A`$ is

```math
\boxed{\mathcal E_{\min}(A,T,m)=\frac{2\pi}{T}\,\Phi_m(A).}
\qquad\text{(6)}
```

The prescribed data include the diagonal of $`A`$. The minimum is attained by a finite Fourier sum. No temporal-frequency cutoff, pulse-segmentation constraint, or bound on instantaneous force is assumed in this theorem.

The positive and negative spectra have separate harmonic resources. At a fixed positive harmonic magnitude $`k`$, the $`m`$ complex mode amplitudes supply at most $`2m`$ real directions of each sign. A direction assigned to harmonic $`k`$ costs $`2\pi k`$ units of action per unit eigenvalue magnitude.

### 2.1 Fourier representation for the entire control class

For each mode define the Fourier coefficients of the force by

```math
b_{\ell k}=\frac1T\int_0^T u_\ell(t)e^{-2\pi ikt/T}\,dt,
\qquad k\in\mathbb Z.
\qquad\text{(7)}
```

Closure is exactly $`b_{\ell0}=0`$. Put

```math
c_{\ell k}=\frac{T}{2\pi ik}\,b_{\ell k},\qquad k\ne0.
\qquad\text{(8)}
```

Then

```math
\alpha_\ell(t)=\sum_{k\ne0}
c_{\ell k}\bigl(e^{2\pi ikt/T}-1\bigr).
\qquad\text{(9)}
```

Parseval's identity gives $`\sum_{\ell,k\ne0}k^2\lVert c_{\ell k}\rVert^2<\infty`$. In addition,

```math
\sum_{k\ne0}\lVert c_{\ell k}\rVert
\le
\left(\sum_{k\ne0}k^2\lVert c_{\ell k}\rVert^2\right)^{1/2}
\left(\sum_{k\ne0}k^{-2}\right)^{1/2}<\infty.
\qquad\text{(10)}
```

Thus (9) converges absolutely and uniformly. Its partial sums have zero values at both endpoints and their derivatives converge to $`u_\ell`$ in $`L^2`$. They converge to $`\alpha_\ell`$ in $`H^1`$ as well. Conversely, coefficients satisfying the weighted square-summability condition define an admissible path through (9).

For a finite Fourier sum, orthogonality of the harmonics yields

```math
A=2\pi\sum_{\ell=1}^{m}\sum_{k\ne0}
k\,\mathrm{Re}(c_{\ell k}c_{\ell k}^\dagger),
\qquad
T\mathcal E=4\pi^2\sum_{\ell=1}^{m}\sum_{k\ne0}
k^2\lVert c_{\ell k}\rVert^2.
\qquad\text{(11)}
```

These identities extend to the infinite series. The phase integral is continuous under uniform convergence of the paths and $`L^2`$ convergence of their derivatives. The matrix series is absolutely convergent in trace norm because

```math
\sum_{\ell,k\ne0}|k|
\left\lVert\mathrm{Re}(c_{\ell k}c_{\ell k}^\dagger)\right\rVert_1
=\sum_{\ell,k\ne0}|k|\lVert c_{\ell k}\rVert^2
\le\sum_{\ell,k\ne0}k^2\lVert c_{\ell k}\rVert^2<\infty.
\qquad\text{(12)}
```

Here $`\mathrm{Re}(cc^\dagger)`$ is positive semidefinite as a real matrix: writing $`c=x+iy`$ gives $`\mathrm{Re}(cc^\dagger)=xx^{\mathsf T}+yy^{\mathsf T}`$. This also proves the trace-norm equality used in (12). Positive and negative Fourier indices are independent because the paths and forces are complex; no conjugacy constraint relates them.

### 2.2 A weighted positive-decomposition lemma

**Lemma 2.** Suppose $`P_k\succeq0`$ are real symmetric matrices of size $`n`$, $`\mathrm{rank}P_k\le d`$, and $`\sum_{k\ge1}k\mathrm{tr}P_k<\infty`$. If $`P=\sum_{k\ge1}P_k`$ and $`\lambda_1(P)\ge\cdots\ge\lambda_n(P)\ge0`$, then

```math
\sum_{k\ge1}k\mathrm{tr}P_k
\ge\sum_{r=1}^{n}\left\lceil\frac r d\right\rceil\lambda_r(P).
\qquad\text{(13)}
```

**Proof.** Let $`S_q=\sum_{k=1}^{q}P_k`$, with $`S_0=0`$. Then $`0\preceq S_q\preceq P`$ and $`\mathrm{rank}S_q\le dq`$. If $`\Pi_q`$ is the orthogonal projection onto the range of $`S_q`$, the variational principle for sums of ordered eigenvalues gives

```math
\mathrm{tr}S_q
=\mathrm{tr}(\Pi_q S_q)
\le\mathrm{tr}(\Pi_q P)
\le\sum_{r=1}^{\min(dq,n)}\lambda_r(P).
\qquad\text{(14)}
```

Consequently,

```math
\mathrm{tr}(P-S_q)\ge\sum_{r>dq}\lambda_r(P).
\qquad\text{(15)}
```

Sum this inequality over $`q=0,1,\ldots`$. All summands are nonnegative, so Tonelli's theorem applies:

```math
\begin{aligned}
\sum_{k\ge1}k\mathrm{tr}P_k
&=\sum_{q\ge0}\mathrm{tr}(P-S_q)\\
&\ge\sum_{q\ge0}\sum_{r>dq}\lambda_r(P)
=\sum_{r=1}^{n}\left\lceil\frac r d\right\rceil\lambda_r(P).
\end{aligned}
\qquad\text{(16)}
```

Each $`P_k`$ occurs in exactly $`k`$ of the tails on the first line; each eigenvalue $`\lambda_r(P)`$ occurs in exactly $`\lceil r/d\rceil`$ tails on the second. This proves the lemma. Equality is obtained by grouping the descending spectral rank-one terms of $`P`$ into successive batches of at most $`d`$. $`\square`$

### 2.3 Signed contributions and the lower bound

Separate the positive and negative Fourier indices in (11). For $`k\ge1`$, define

```math
P_k=2\pi k\sum_{\ell=1}^{m}
\mathrm{Re}(c_{\ell k}c_{\ell k}^\dagger),
\qquad
Q_k=2\pi k\sum_{\ell=1}^{m}
\mathrm{Re}(c_{\ell,-k}c_{\ell,-k}^\dagger).
\qquad\text{(17)}
```

Both are positive semidefinite and each has rank at most $`2m`$. With $`P=\sum_{k\ge1}P_k`$ and $`Q=\sum_{k\ge1}Q_k`$, equations (11) become

```math
A=P-Q,\qquad
\frac{T\mathcal E}{2\pi}
=\sum_{k\ge1}k\bigl[\mathrm{tr}P_k+\mathrm{tr}Q_k\bigr].
\qquad\text{(18)}
```

Apply Lemma 2 separately to $`P`$ and $`Q`$ with $`d=2m`$. Since $`A\preceq P`$ and $`-A\preceq Q`$, monotonicity of ordered eigenvalues implies

```math
\lambda_r(P)\ge\lambda_r^+(A),\qquad
\lambda_r(Q)\ge\lambda_r^-(A)
\quad (1\le r\le n).
\qquad\text{(19)}
```

The zero padding causes no difficulty because $`P`$ and $`Q`$ are positive semidefinite. Therefore

```math
\frac{T\mathcal E}{2\pi}
\ge\sum_{r=1}^{n}\left\lceil\frac r{2m}\right\rceil
\bigl[\lambda_r(P)+\lambda_r(Q)\bigr]
\ge\Phi_m(A).
\qquad\text{(20)}
```

This step permits arbitrary cancellation between the two signs, including noncommuting $`P`$ and $`Q`$. Only the eigenvalue inequalities (19) are used. The stronger matrix assertion $`P\succeq A_+`$, with $`A_+`$ the positive spectral part of $`A`$, is generally false and is not needed.

### 2.4 Attainment with finitely many harmonics

Choose real orthonormal eigenvectors and set

```math
p_r=\sqrt{\lambda_r^+(A)}\,v_r^+,
\qquad
q_r=\sqrt{\lambda_r^-(A)}\,v_r^-,
\qquad
A=\sum_r p_rp_r^{\mathsf T}-\sum_r q_rq_r^{\mathsf T}.
\qquad\text{(21)}
```

Set $`p_r`$ or $`q_r`$ to zero after the corresponding list ends. For each $`k\ge1`$ and $`1\le\ell\le m`$, put

```math
r_1=2m(k-1)+2\ell-1,\qquad r_2=r_1+1,
\qquad\text{(22)}
```

and choose

```math
c_{\ell k}=\frac{p_{r_1}+ip_{r_2}}{\sqrt{2\pi k}},
\qquad
c_{\ell,-k}=\frac{q_{r_1}+iq_{r_2}}{\sqrt{2\pi k}}.
\qquad\text{(23)}
```

The real and imaginary quadratures contribute their two real rank-one matrices without cross terms in $`\mathrm{Re}(cc^\dagger)`$. Thus (11) gives exactly the prescribed $`A`$. The energy identity gives

```math
T\mathcal E
=2\pi\sum_{k\ge1}k\sum_{r=2m(k-1)+1}^{2mk}
\bigl[\lambda_r^+(A)+\lambda_r^-(A)\bigr]
=2\pi\Phi_m(A).
\qquad\text{(24)}
```

Use (9) for the path and differentiate it for the force. Closure is exact, and only harmonics with

```math
1\le |k|\le
\left\lceil\frac{\max(n_+,n_-)}{2m}\right\rceil
\qquad\text{(25)}
```

are needed, where $`n_+`$ and $`n_-`$ are the numbers of positive and negative eigenvalues. For $`A=0`$, the zero control suffices. This completes the proof of Theorem 1.

For a normalization check, one scalar positive entry $`A=a`$ is produced by $`\alpha(t)=\sqrt{a/(2\pi)}(e^{2\pi it/T}-1)`$. Its phase integral is $`a`$ and its action is $`2\pi a`$. The phase integral is twice the ordinary oriented area of this circle in its two real quadratures.

## 3. A bound in terms of singular values

Let $`s_1(A)\ge\cdots\ge s_n(A)\ge0`$ be the singular values of $`A`$. They are the merged positive and negative eigenvalue magnitudes. Theorem 1 implies

```math
\boxed{
T\mathcal E\ge2\pi\sum_{r=1}^{n}
\left\lceil\frac r{4m}\right\rceil s_r(A).
}
\qquad\text{(26)}
```

To see this directly, express the two weighted spectral sums in (5) as tails:

```math
\Phi_m(A)=\sum_{q\ge0}
\left[\sum_{r>2mq}\lambda_r^+(A)
+\sum_{r>2mq}\lambda_r^-(A)\right].
\qquad\text{(27)}
```

At each $`q`$, the two omitted prefixes contain at most $`4mq`$ singular values. Their sum is at most the sum of the $`4mq`$ largest singular values. Hence the bracket in (27) is at least $`\sum_{r>4mq}s_r(A)`$. Summing the tails proves (26).

Equation (26) relaxes the distinction between positive and negative harmonic resources. It can be weaker than the exact formula for a specified $`A`$, but its dependence only on singular values makes it useful for submatrix and determinant arguments. Section 6 retains the block structure and obtains the stronger sharp cross-block form used in the [physical gate converse](gate_layer_bounds.md).

## 4. A phase matrix and a physical gate have different optimization domains

Fix a quadratic target $`U_{A_0}=\exp(iZ^{\mathsf T}A_0Z)`$ and permit a global phase and free final local $`Z`$ rotations. The real symmetric matrices representing the same target are exactly

```math
\mathscr R(A_0)=
\left\{A_0+D+\frac\pi4N:
D\text{ real diagonal},\quad
N=N^{\mathsf T},\quad N_{ij}\in\mathbb Z,\quad N_{ii}=0\right\}.
\qquad\text{(28)}
```

For necessity, evaluate the relative phase on the four sign configurations obtained by independently flipping $`z_i,z_j\in\{\pm1\}`$. The mixed difference removes all local and constant phases and gives $`8(A-A_0)_{ij}\in2\pi\mathbb Z`$. For sufficiency, each permitted off-diagonal shift contributes

```math
\exp\!\left(\frac{i\pi}{2}N_{ij}Z_iZ_j\right)
=i^{N_{ij}}(Z_iZ_j)^{N_{ij}},
\qquad\text{(29)}
```

a product of local $`Z`$ operators up to a global phase. The diagonal contributes only a global phase.

It follows from Theorem 1 that the exact gate-level optimal action in this equivalence class is

```math
\min_{A\in\mathscr R(A_0)}2\pi\Phi_m(A).
\qquad\text{(30)}
```

The minimum exists: $`\mathscr R(A_0)`$ is closed, $`\Phi_m`$ is continuous, and $`\Phi_m(A)\ge\lVert A\rVert_*`$ makes its sublevel sets bounded. This variational characterization does not solve the integer optimization in closed form. The freedom in (28) is essential: even the identity channel admits representatives with nonzero spectrum. A lower bound evaluated only at a chosen diagonal or a chosen real logarithm does not bound every realization of the physical gate. The [gate-layer analysis](gate_layer_bounds.md) controls the entire class (28), and its fixed-error extension, by a constraint on the cross block of the phase matrix. The [matching construction](matching_construction.md) chooses useful diagonal representatives and applies the harmonic allocation above to obtain the matching order of resource cost.

## 5. Relation to the classical spectral area problem

Brockett's Theorem 2 and the explicit vertical-distance formula in Rizzi–Serres, Appendix A, Proposition 15, connect minimum control energy to integer-weighted area spectra. In the latter paper's normalization, let $`Y`$ be a real skew-symmetric area matrix with nonzero eigenvalues $`\pm i\mu_r`$, where $`\mu_1\ge\cdots\ge\mu_s>0`$. The minimum action for a closed real path with prescribed $`Y`$ is

```math
\min T\int_0^T\lVert\dot q(t)\rVert^2\,dt
=4\pi\sum_{r=1}^{s}r\mu_r,
\qquad
Y=\frac12\int_0^T
\bigl(q\dot q^{\mathsf T}-\dot q q^{\mathsf T}\bigr)\,dt.
\qquad\text{(31)}
```

This is their squared sub-Riemannian distance to a vertical endpoint; constant-speed parametrization identifies it with the minimum action. See [Rizzi–Serres, Appendix A](https://arxiv.org/html/1610.01596v2#A1), which also discusses the normalization difference from Brockett's formula.

The [author-linked erratum](https://drive.google.com/file/d/1uSMry_CAEsKCGpL39tgO8ND7TX48HHLG/view) corrects a codimension statement in Proposition 4 and restores missing skew-symmetric $`J_2`$ blocks in Eq. (50). It leaves Proposition 15 and its distance formula, Eq. (48), unchanged; (31) uses that formula.

The map to the present problem can be derived explicitly. Write $`\alpha_\ell=x_\ell+iy_\ell`$ and concatenate

```math
q=(x_1,y_1,\ldots,x_m,y_m)\in\mathbb R^{2mn}.
\qquad\text{(32)}
```

Then $`\lVert\dot q\rVert^2=\sum_\ell\lVert u_\ell\rVert^2`$. For the area matrix in (31), integration by parts along the closed path gives

```math
Y_{x_{\ell,i},y_{\ell,j}}
=\int_0^T x_{\ell,i}\dot y_{\ell,j}\,dt.
\qquad\text{(33)}
```

Here the subscripts label coordinates of $`q`$. Consequently the phase observable is the linear image

```math
A_{ij}=\sum_{\ell=1}^{m}
\left[Y_{x_{\ell,i},y_{\ell,j}}
+Y_{x_{\ell,j},y_{\ell,i}}\right]
\equiv\mathcal L(Y)_{ij}.
\qquad\text{(34)}
```

Thus prescribing $`A`$ leaves many components of $`Y`$ free: the same-mode $`x`$–$`x`$ and $`y`$–$`y`$ areas, cross-mode areas, and parts of the $`x`$–$`y`$ blocks are unobserved. In geometric language, this is a quotient of the free step-two area system by a subspace of its center. In optimization language, it minimizes (31) over all skew area matrices satisfying $`\mathcal L(Y)=A`$.

Equations (6) and (34) therefore give the explicit projected-area identity

```math
\min_{\mathcal L(Y)=A}
4\pi\sum_{r=1}^{s(Y)}r\mu_r(Y)
=2\pi\Phi_m(A).
\qquad\text{(35)}
```

The Fourier proof evaluates this projection with its $`2m`$ real directions per sign and harmonic. The classical weighted-spectrum principle is the antecedent; the separate gate-equivalence and finite-error arguments are needed to obtain the architecture-level converse. The [related-work account](../references/related_work.md) places these mathematical and gate-synthesis ingredients in their broader context.

## 6. Sharp cost when only a cross block is prescribed

Let $`\mathsf A,\mathsf B`$ be disjoint sets of qubit coordinates, and put $`C=A_{\mathsf A\mathsf B}`$. Write its descending singular values as $`s_j(C)`$, with zeros appended.

**Theorem 3 — sharp cross-block cost.** Every real symmetric completion of $`C`$ obeys

```math
\boxed{\Phi_m(A)\ge
2\sum_{j\ge1}\left\lceil\frac j{4m}\right\rceil s_j(C).}
\qquad\text{(36)}
```

Consequently every closed trajectory satisfies

```math
\boxed{T\mathcal E\ge
4\pi\sum_{j\ge1}\left\lceil\frac j{4m}\right\rceil s_j(C).}
\qquad\text{(37)}
```

In particular, $`T\mathcal E\ge4\pi\lVert C\rVert_*`$ and $`T\mathcal E\ge(\pi/m)\sum_jj s_j(C)`$. If both diagonal blocks may be chosen freely, equality in (36)–(37) is attainable.

**Proof of the converse.** For every real symmetric block matrix $`R`$,

```math
\lVert R\rVert_*\ge2\lVert R_{\mathsf A\mathsf B}\rVert_*.
\qquad\text{(38)}
```

Indeed, place the polar partial isometry of the cross block and its transpose in the two off-diagonal blocks of a symmetric matrix, with zeros elsewhere. This matrix has operator norm at most one, and its trace pairing with $`R`$ is $`2\lVert R_{\mathsf A\mathsf B}\rVert_*`$. Nuclear/operator-norm duality proves (38).

For $`q\ge0`$, let $`A^{(q)}`$ retain the first $`2mq`$ positive eigenvectors and the first $`2mq`$ negative eigenvectors of $`A`$. It has rank at most $`4mq`$, and its cross block is a rank-at-most-$`4mq`$ approximation to $`C`$. The best-rank approximation characterization of nuclear-norm tails and (38) give

```math
\begin{aligned}
\sum_{j>2mq}[\lambda_j^+(A)+\lambda_j^-(A)]
&=\lVert A-A^{(q)}\rVert_*\\
&\ge2\lVert C-(A^{(q)})_{\mathsf A\mathsf B}\rVert_*\\
&\ge2\sum_{j>4mq}s_j(C).
\end{aligned}
```

Sum over $`q\ge0`$ as in (27). The two tails count the weights $`\lceil j/(2m)\rceil`$ and $`\lceil j/(4m)\rceil`$, proving (36). Theorem 1 then proves (37). This retains both symmetric copies of the cross block, which are lost in the coordinate-compression relaxation of (26).

**Sharp completion.** Take a real singular-value decomposition $`C=\sum_js_j u_jv_j^{\mathsf T}`$. In every consecutive batch of $`4m`$ singular directions, assign the first $`2m`$ sign $`\tau_j=+1`$ and the remaining $`2m`$ sign $`\tau_j=-1`$. Set

```math
q_j=\frac{u_j\oplus\tau_jv_j}{\sqrt2},\qquad
A_* =\sum_j2\tau_j s_j q_jq_j^{\mathsf T}.
\qquad\text{(39)}
```

Its cross block is $`C`$; its nonzero eigenvalues are $`2\tau_js_j`$. Within each sign, the magnitudes remain in descending order and have harmonic weight $`\lceil j/(4m)\rceil`$. Hence $`\Phi_m(A_*)=2\sum_j\lceil j/(4m)\rceil s_j(C)`$, and Theorem 1 supplies attaining trajectories.

For a general $`C`$, these diagonal blocks can contain unwanted same-side interactions. Thus the completion alone is not an upper bound for every prescribed physical gate. For $`C=cI_K`$, the singular vectors are coordinate vectors and both blocks are ordinary diagonal matrices. Their only gate effect is global phase; this is the [matching construction](matching_construction.md).

## 7. Phase, exposure, and trajectory energy

Collect the closed trajectories into $`D(t)\in\mathbb C^{m\times n}`$, with $`D_{\ell j}=\alpha_{j\ell}`$. Define

```math
F=\mathrm{Re}\int_0^T D^\dagger D\,dt,\quad
E_{\rm mat}=\mathrm{Re}\int_0^T\dot D^\dagger\dot D\,dt,\quad
X=\mathrm{tr}F,\quad
E_{\rm path}=\mathrm{tr}E_{\rm mat}.
\qquad\text{(40)}
```

Here $`E_{\rm path}=\mathcal E`$ for the lossless force $`u=\dot D`$. Keeping a closed path under vacuum damping requires $`u=\dot D+\kappa D/2`$, so its paid fluence instead is $`\mathcal E=E_{\rm path}+\kappa^2X/4`$. The [loss account](loss_and_frontier.md) derives the physical channel and the exact priced optimum.

The trajectories and $`-i`$ times their derivatives form a real Gram matrix:

```math
\begin{pmatrix}F&A\\A&E_{\rm mat}\end{pmatrix}\succeq0,
\qquad
\ker F\subseteq\ker A,\qquad
E_{\rm mat}\succeq AF^+A.
\qquad\text{(41)}
```

The Moore–Penrose inverse $`F^+`$ handles singular exposure. If $`S`$ is the real symmetric orthogonal sign matrix of $`A`$, extended by arbitrary signs on its kernel, Cauchy–Schwarz applied to the area pairing gives

```math
E_{\rm path}X\ge\lVert A\rVert_*^2.
\qquad\text{(42)}
```

Closure supplies the stronger scalar inequality

```math
\boxed{E_{\rm path}\ge
\frac{\lVert A\rVert_*^2}{X}+\frac{\pi^2}{T^2}X,\qquad X>0.}
\qquad\text{(43)}
```

To prove it, apply Dirichlet Poincaré to $`B(t)=D(t)e^{-i\omega St}`$. Direct differentiation yields

```math
\int_0^T\lVert\dot B\rVert_F^2dt
=E_{\rm path}-2\omega\lVert A\rVert_*+\omega^2X
\ge\frac{\pi^2}{T^2}X.
```

Optimize over real $`\omega`$ to obtain (43). When the positive and negative ranks are each at most $`2m`$, equality is attainable. In a real eigenbasis of $`A`$, use columns proportional to $`\sin(\pi t/T)e^{i\operatorname{sign}(\lambda_j)\omega t}`$, with coefficient vectors real-orthogonal within each sign and scaled to the required area. The opposite-sign cross areas vanish by integration of a boundary derivative. Higher ranks require further temporal directions, as quantified by Theorem 1 and the [priced area spectrum](loss_and_frontier.md#3-spectrum-of-the-closed-loop-area-operator).

### The finite-time term cannot be added as a matrix inequality

The stronger assertion $`E_{\rm mat}\succeq AF^+A+(\pi/T)^2F`$ is false. For one mode and two columns, take

```math
\alpha_1(t)=\sin(\pi t/T)e^{i\pi t/T},\qquad
\alpha_2(t)=\sin(\pi t/T)e^{-i\pi t/T}.
```

Direct integration gives

```math
F=\frac T4\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
A=\frac\pi2\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E_{\rm mat}=\frac{\pi^2}{T}I_2.
```

The proposed matrix residual is

```math
E_{\rm mat}-AF^{-1}A-\frac{\pi^2}{T^2}F
=\frac{\pi^2}{T}\begin{pmatrix}-1/6&7/12\\7/12&-1/6\end{pmatrix},
```

with eigenvalues $`(\pi^2/T)\{5/12,-3/4\}`$. The scalar inequality (43) is nevertheless saturated. It must not be inferred from that false matrix strengthening.

## Primary sources

- **WongBaillieul2012:** W. S. Wong and J. Baillieul, “Control Communication Complexity of Distributed Actions,” Theorem 5.1 and Corollary 5.1. [Author preprint](https://arxiv.org/abs/1201.6527v2). These establish the inherited weighted bilinear-control method; the proofs here fix its symmetric phase and multimode normalization.
- **Brockett1982:** R. W. Brockett, “Control theory and singular Riemannian geometry,” in *New Directions in Applied Mathematics*, pp. 11–27 (Springer, 1982), especially Theorem 2. [Author-hosted reprint](https://hrl.harvard.edu/publications/brockett81control.pdf); the reprint bears a 1981 copyright date.
- **RizziSerres2017:** L. Rizzi and U. Serres, “On the cut locus of free, step two Carnot groups,” *Proceedings of the American Mathematical Society* **145**, 5341–5357 (2017), Appendix A, Proposition 15 and Eq. (48). [DOI](https://doi.org/10.1090/proc/13658); [author preprint](https://arxiv.org/html/1610.01596v2).
- **RizziSerresErrata:** L. Rizzi and U. Serres, “Errata to: On the cut locus of free, step two Carnot groups,” undated. [Erratum](https://drive.google.com/file/d/1uSMry_CAEsKCGpL39tgO8ND7TX48HHLG/view), linked from [Luca Rizzi's research page](https://sites.google.com/view/rizziluca/research).
