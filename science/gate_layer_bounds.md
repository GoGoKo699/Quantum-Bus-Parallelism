# Gate-layer lower bounds with arbitrary phase wraps

The [model](model.md) permits independently controlled commuting linear forces, exact return of every conditional oscillator displacement, and arbitrary final local $`Z`$ corrections. The target is

```math
V_K=\prod_{j=1}^K\exp(i\pi Z_{A_j}Z_{B_j}/4).
```

This account proves a lower bound for the physical gate, including every allowed logarithm of that gate. It also proves robustness at fixed worst-case error for the entire layer. The [matching construction](matching_construction.md) attains the resulting order of growth.

## 1. Statement and spectral input

Write $`\mathcal A=\mathcal ET`$ for force fluence multiplied by duration, and define

```math
c=\frac\pi8,\qquad
w_r=\left\lceil\frac r{4m}\right\rceil,\qquad
G_{K,m}=\left(\prod_{r=1}^K w_r\right)^{1/K},\qquad
\lVert w\rVert_2=\left(\sum_{r=1}^K w_r^2\right)^{1/2}.
\qquad\text{(1)}
```

**Theorem.** Let $`K,m\ge1`$ be integers. Suppose the closed-loop gate $`U_A=\exp(iZ^{\mathsf T}AZ)`$ has layer error

```math
\epsilon(A)=\inf_\theta\frac12
\left\lVert\mathcal U_A-\mathcal L(\theta)\circ\mathcal V_K\right\rVert_\diamond
\le\epsilon<\frac1{\sqrt2},
\qquad \delta=\arcsin\epsilon.
\qquad\text{(2)}
```

Then

```math
\boxed{\displaystyle
\mathcal ET\ge
\frac{\pi^2}{2}K G_{K,m}-2\pi\delta\lVert w\rVert_2
\ge
\frac{\pi^2}{2}\left(1-\frac{4\delta}{\pi}\right)K G_{K,m}.}
\qquad\text{(3)}
```

In particular, for all $`K,m`$ in the stated range,

```math
\mathcal ET\ge
\frac{\pi^2}{2(1+4e)}
\left(1-\frac{4\arcsin\epsilon}{\pi}\right)
\left(K+\frac{K^2}{m}\right).
\qquad\text{(4)}
```

At $`\epsilon=0`$, (3) gives the exact-gate converse
$`\mathcal ET\ge(\pi^2/2)K G_{K,m}`$. The proof uses no bound on the size or conditioning of the integer phase wraps. The threshold in (2) is a sufficient range proved here; optimality of that threshold is not claimed.

The only control-theoretic input is the [spectral cost theorem](spectral_cost.md). For the singular values $`s_1(A)\ge s_2(A)\ge\cdots`$, that theorem implies

```math
\mathcal ET\ge2\pi\sum_{r\ge1}
\left\lceil\frac r{4m}\right\rceil s_r(A).
\qquad\text{(5)}
```

Let $`C=A_{AB}`$ denote the $`K\times K`$ cross block between the two sides of the matching. Coordinate compression gives $`s_r(C)\le s_r(A)`$, so (5) already supplies a valid converse. The [sharp cross-block theorem](spectral_cost.md#6-sharp-cost-when-only-a-cross-block-is-prescribed) retains both symmetric copies of this block and strengthens that relaxation to

```math
\mathcal ET\ge4\pi\sum_{r=1}^K w_r s_r(C).
\qquad\text{(6)}
```

All subsequent steps concern gate equivalence and finite-dimensional matrices.

## 2. Exact gates force an odd-determinant cross block

Use signs $`z_j\in\{-1,1\}`$ and Boolean coordinates $`x_j=(1-z_j)/2`$. Exact equality up to local and global phases says that

```math
q(x)=z^{\mathsf T}Az-
\frac\pi4\sum_{j=1}^K z_{A_j}z_{B_j}
-\sum_j\theta_jz_j-\phi
=2\pi k(x),\qquad k(x)\in\mathbb Z.
\qquad\text{(7)}
```

The function $`q`$ is a multilinear polynomial of degree at most two on the Boolean cube. The coefficients of an integer-valued Boolean function in its unique multilinear representation are integers: the coefficient on a set of coordinates $`S`$ is the finite difference $`\Delta_S k(0)`$. Consequently the quadratic coefficients of $`k`$ in (7) are integers.

Because $`A`$ is symmetric, the coefficient of $`x_{A_i}x_{B_j}`$ in $`z^{\mathsf T}Az`$ is $`8C_{ij}`$. The corresponding target coefficient is $`\pi\delta_{ij}`$. It follows that

```math
8(C-cI)=2\pi M,
\qquad
C=c(I+2M),\qquad M\in\mathbb Z^{K\times K}.
\qquad\text{(8)}
```

These are physical phase wraps. A shift of an off-diagonal matrix entry by $`\pi n/4`$ changes the gate by

```math
\exp(i\pi n Z_iZ_j/2)=(iZ_iZ_j)^n,
```

which is a product of local $`Z`$ operators and a global phase. Thus every cross-block shift in (8) is allowed. Conditions on the other off-diagonal entries are not needed for the converse.

The integer matrix $`I+2M`$ reduces to the identity modulo two. Its determinant is an odd integer, so it is nonzero and has absolute value at least one. Therefore

```math
\prod_{r=1}^K s_r(C)=|\det C|\ge c^K.
\qquad\text{(9)}
```

Applying arithmetic–geometric mean to the $`K`$ nonnegative numbers $`w_rs_r(C)`$ in (6) gives

```math
\mathcal ET\ge4\pi K
\left(\prod_{r=1}^K w_rs_r(C)\right)^{1/K}
\ge4\pi cK G_{K,m}.
\qquad\text{(10)}
```

This proves the exact part of the theorem.

## 3. Half-diamond error gives a uniform phase lift

The normalization in (2) is **half** the diamond norm. The following standard unitary-channel fact is recalled with a proof to make the phase range explicit; see Haah, Kothari, O'Donnell, and Tang, Appendix A, for a primary-source treatment of the same numerical-range formula [1].

**Spectral-arc lemma.** For two finite-dimensional unitary channels let
$`d=\tfrac12\lVert\mathcal U-\mathcal V\rVert_\diamond<1`$.
After an overall phase rotation, all eigenvalues of $`V^\dagger U`$ have arguments in $`[-\arcsin d,\arcsin d]`$.

**Proof.** Put $`W=V^\dagger U`$. For a pure input on the system and a reference, the two pure output states have overlap $`\mathrm{tr}(\rho W)`$, where $`\rho`$ is the reduced state of the system. Their trace distance is $`\sqrt{1-|\mathrm{tr}(\rho W)|^2}`$. Maximizing over inputs gives

```math
d=\sqrt{1-\nu^2},\qquad
\nu=\min\left\{|z|:z\in\mathrm{conv}(\mathrm{spec}W)\right\}.
\qquad\text{(11)}
```

Indeed $`\mathrm{tr}(\rho W)`$ ranges over that convex hull, and every such value is attained. Since $`d<1`$, the hull excludes the origin and the eigenvalues lie in an open semicircle. Let their shortest containing arc have width $`\vartheta<\pi`$ and rotate its midpoint to argument zero. Every point in the hull then has real part at least $`\cos(\vartheta/2)`$. The midpoint of the chord between the two arc endpoints attains this distance from the origin. Hence $`\nu=\cos(\vartheta/2)`$ and $`d=\sin(\vartheta/2)`$, as required. The singleton-spectrum case has $`\vartheta=0`$. $`\square`$

Apply this lemma to $`U_A`$ and a local correction of $`V_K`$ attaining the infimum in (2). Such a correction exists because the local phase parameters range over a compact torus. After a further global phase choice, the diagonal relative unitary has a real phase lift

```math
q(x)=2\pi k(x)+r(x),\qquad
k(x)\in\mathbb Z,\qquad |r(x)|\le\delta<\pi/4,
\qquad\text{(12)}
```

where $`q`$ is the quadratic polynomial in (7). The integer function $`k`$ need not initially be assumed to be polynomial of low degree. Proving that fact is the next step.

## 4. Small uniform error forces quadratic integer wraps

For a Boolean function define $`\Delta_i f`$ by subtracting its value at $`x_i=0`$ from its value at $`x_i=1`$, with all other coordinates fixed. For distinct coordinates $`i,j,\ell`$ and every assignment of the remaining coordinates,

```math
0=\Delta_i\Delta_j\Delta_\ell q
=2\pi\Delta_i\Delta_j\Delta_\ell k
+\Delta_i\Delta_j\Delta_\ell r.
\qquad\text{(13)}
```

The last term is a signed sum of eight residual values, so its absolute value is at most $`8\delta<2\pi`$. The other term is an integer multiple of $`2\pi`$. They can cancel only if both terms vanish. Every third difference of $`k`$ is therefore zero.

To see that this is enough, the multilinear coefficient on any set $`S`$ with $`|S|\ge3`$ is $`\Delta_Sk(0)`$. Factor this into a third difference followed by the differences on the remaining coordinates. It vanishes because the third difference is zero at every basepoint. Thus $`k`$ has degree at most two; its coefficients are integers as before. For fewer than three coordinates the degree assertion holds automatically. Equation (12) then also makes $`r`$ a quadratic Boolean function.

Extracting cross coefficients as in (8) gives

```math
C=D+R,\qquad D=c(I+2M),\qquad M\in\mathbb Z^{K\times K}.
\qquad\text{(14)}
```

In sign coordinates $`a,b\in\{-1,1\}^K`$, the part of $`r(a,b)`$ involving both sides of the matching is $`2a^{\mathsf T}Rb`$. All constant, linear, and within-side quadratic terms disappear from the four-point difference

```math
r(a,b)-r(a,-b)-r(-a,b)+r(-a,-b)
=8a^{\mathsf T}Rb.
\qquad\text{(15)}
```

The left side has absolute value at most $`4\delta`$. Hence

```math
\max_{a,b\in\{-1,1\}^K}|a^{\mathsf T}Rb|\le\delta/2.
\qquad\text{(16)}
```

Average the square over independent uniform sign vectors. Independence gives
$`\mathbb E(a^{\mathsf T}Rb)^2=\sum_{ij}R_{ij}^2`$. Consequently

```math
\boxed{\lVert R\rVert_F\le\delta/2.}
\qquad\text{(17)}
```

The bound is on the whole cross block, with no factor of $`K`$. A separate entrywise estimate would lose this information. Equivalently, (17) follows by applying Boolean Parseval to the cross Fourier coefficients $`2R_{ij}`$ of the bounded quadratic function $`r`$.

## 5. A weighted singular-value perturbation bound

Mirsky's Frobenius perturbation inequality [2] states

```math
\sum_{r=1}^K\bigl(s_r(C)-s_r(D)\bigr)^2
\le\lVert C-D\rVert_F^2.
\qquad\text{(18)}
```

For completeness, its special case here follows from the trace inequality
$`\mathrm{Re}\mathrm{tr}(C^\dagger D)\le\sum_rs_r(C)s_r(D)`$.
Expand $`\lVert C-D\rVert_F^2`$, and use $`\lVert C\rVert_F^2=\sum_rs_r(C)^2`$ and the corresponding identity for $`D`$. This gives exactly (18).

The determinant argument applies to $`D`$ regardless of its condition number, so
$`\sum_rw_rs_r(D)\ge cK G_{K,m}`$. Equations (17), (18), and Cauchy–Schwarz yield

```math
\begin{aligned}
\sum_{r=1}^K w_rs_r(C)
&\ge\sum_{r=1}^K w_rs_r(D)
-\lVert w\rVert_2
\left(\sum_{r=1}^K(s_r(C)-s_r(D))^2\right)^{1/2}\\
&\ge cK G_{K,m}-\frac\delta2\lVert w\rVert_2.
\end{aligned}
\qquad\text{(19)}
```

Combining this with (6) proves the first inequality of (3). The error penalty depends on the Euclidean norm of the weights, rather than their sum. This is what preserves the action bound even when a phase-wrapped representative has extremely small singular values.

## 6. Uniform constants for every $`K`$ and $`m`$

We prove the elementary staircase-weight estimate

```math
\lVert w\rVert_2\le K G_{K,m}.
\qquad\text{(20)}
```

Set $`q=4m\ge4`$ and $`J=\lceil K/q\rceil`$. If $`J\ge2`$, the weights contain $`q`$ copies of each of $`1,\ldots,J-1`$, followed by between one and $`q`$ copies of $`J`$. Therefore

```math
G_{K,m}\ge\bigl((J-1)!\bigr)^{1/(J-1)}\ge J/e.
\qquad\text{(21)}
```

For the last inequality, put $`n=J-1\ge1`$ and use

```math
\log(n!)\ge\int_1^n\log x\,dx
=n\log n-n+1
\ge n\log(n+1)-n.
```

The final step is $`n\log(1+1/n)\le1`$. If $`J=1`$, the bound $`G_{K,m}\ge J/e`$ also holds. For $`K\ge8`$,

```math
\lVert w\rVert_2\le\sqrt K\,J
\le\frac e{\sqrt K}K G_{K,m}\le K G_{K,m},
```

because $`e^2<8`$. For $`K\le7`$, either every weight is one, or $`J=2`$ and $`K\ge5`$ because $`q\ge4`$. In the latter case,
$`\lVert w\rVert_2\le2\sqrt K\le K\le K G_{K,m}`$; the all-ones case is immediate. This proves (20) in every case. Substitution into (19) proves the second inequality of (3).

Finally,

```math
G_{K,m}\ge1,\qquad
G_{K,m}\ge\frac{(K!)^{1/K}}{4m}\ge\frac K{4em}.
\qquad\text{(22)}
```

For $`x\ge0`$, $`\max\{1,x/(4e)\}\ge(1+x)/(1+4e)`$. Apply this with $`x=K/m`$ to obtain (4).

## 7. Consequence for a force-limited clock

If every qubit obeys
$`\sum_\ell|u_{j\ell}(t)|^2\le g^2`$ almost everywhere, then
$`\mathcal E\le2Kg^2T`$. Equation (3) gives

```math
T\ge\frac\pi{2g}
\sqrt{\left(1-\frac{4\arcsin\epsilon}{\pi}\right)G_{K,m}},
\qquad\text{(23)}
```

and the explicitly uniform form is

```math
T\ge\frac\pi{2g\sqrt{1+4e}}
\sqrt{\left(1-\frac{4\arcsin\epsilon}{\pi}\right)
\left(1+\frac Km\right)}.
\qquad\text{(24)}
```

The [exact construction](matching_construction.md) has
$`T=(\pi/2g)\sqrt{\lceil K/(4m)\rceil}`$. It proves
$`T_\epsilon(K,m,g)=\Theta_\epsilon(\sqrt{1+K/m}/g)`$ for every fixed error tolerance in (2). Its bandwidth and displacement requirements are separate resources and are stated with the construction.

## 8. Why approximate rank is insufficient

The determinant condition does not keep every singular value away from zero. For example, with an integer $`h>0`$,

```math
B_h=\begin{pmatrix}1&2h\\0&1\end{pmatrix},\qquad
D_h=cB_h
\qquad\text{(25)}
```

satisfies $`B_h\equiv I\pmod2`$ and $`\det B_h=1`$. Its singular values are

```math
s_\pm(D_h)=c\bigl(\sqrt{h^2+1}\pm h\bigr),\qquad
s_-(D_h)=\frac c{\sqrt{h^2+1}+h}.
\qquad\text{(26)}
```

Let $`C_h`$ be its best rank-one approximation. Then
$`\lVert C_h-D_h\rVert_F=s_-(D_h)\to0`$, while the retained singular value diverges. With the full symmetric matrix
$`A_h=\left(\begin{smallmatrix}0&C_h\\C_h^{\mathsf T}&0\end{smallmatrix}\right)`$,
the residual phase on two matched pairs is bounded by
$`2|a^{\mathsf T}(C_h-D_h)b|\le4s_-(D_h)`$.
Thus rank can fall while the physical gate approaches the target, after local correction. Its action remains large: on one mode the prescribed-matrix cost is $`4\pi s_+(D_h)`$, which grows linearly in $`h`$.

The [finite-harmonic boundary proposition](matching_construction.md#6-a-boundary-of-the-exact-harmonic-capacity-law) strengthens this example: for each fixed $`K`$, a rank-two full matrix using only the first positive and negative harmonics can approximate the entire layer arbitrarily well at divergent action. Neither phenomenon contradicts (3). Both show why a robust converse must charge the magnitudes of the surviving singular values.

## 9. Additional finite-size and total-force consequences

The same perturbation argument also gives useful lower bounds without staircase weights. Set $`\eta=4\delta/\pi<1`$ and $`Q_K=\sum_{r=1}^K r^2=K(K+1)(2K+1)/6`$. The determinant of $`D=c(I+2M)`$ gives $`\lVert D\rVert_*\ge cK`$ and $`\sum_rrs_r(D)\ge cK(K!)^{1/K}`$. Equation (18) and Cauchy–Schwarz therefore imply

```math
\boxed{\mathcal ET\ge\frac{\pi^2}{2}
\max\left\{K-\eta\sqrt K,\,
\frac{K(K!)^{1/K}-\eta\sqrt{Q_K}}{4m}\right\}.}
\qquad\text{(27)}
```

Here the spectral inputs are $`\mathcal ET\ge4\pi\lVert C\rVert_*`$ and $`\mathcal ET\ge(\pi/m)\sum_rrs_r(C)`$, proved with the [sharp cross-block theorem](spectral_cost.md#6-sharp-cost-when-only-a-cross-block-is-prescribed). The first term of (27) is positive for every $`K\ge1`$. The weighted bound (3) gives a positive all-size congestion constant directly through the weight estimate in Section 6; the estimates can be combined by taking their maximum. No weighted singular-value expression is assumed to satisfy a norm triangle inequality.

Under a total instantaneous coefficient-force cap $`\sum_{j,\ell}|u_{j\ell}(t)|^2\le P`$, $`\mathcal E\le PT`$. In particular every exact implementation obeys

```math
T^2\ge\frac{\pi^2}{2P}KG_{K,m}.
\qquad\text{(28)}
```

The [matching construction](matching_construction.md#2-exact-action-and-force-limited-duration) has constant total squared force and meets this cap whenever $`T^2\ge(\pi^2/(2P))\sum_rw_r`$. Thus the lossless total-cap optimum is $`\Theta(\sqrt{(K+K^2/m)/P})`$. This constraint differs from the individual cap: writing $`P=Kp`$ makes $`p`$ a per-pair total budget, not a per-qubit one. For $`K\le4m`$, all $`w_r=1`$, and the exact action optimum over all phase representatives is $`\pi^2K/2`$; the per-qubit duration optimum is $`\pi/(2g)`$.

### Exact endpoint-local equivalence

For exact gates only, allowing arbitrary product one-qubit unitaries before and after the bus interval gives the same lift constraint. If a diagonal unitary is related to the disjoint matching by such endpoint products, it factors over the same pairs. Each two-qubit factor must be diagonal up to a scalar: an off-diagonal entry in one factor, together with nonzero entries of the others, would otherwise create a nonzero off-diagonal entry in the tensor product. Up to local diagonal phases, a diagonal two-qubit factor is $`e^{i\gamma Z\otimes Z}`$. Its two operator-Schmidt coefficients are $`2|\cos\gamma|`$ and $`2|\sin\gamma|`$. Local equivalence to CZ makes both $`\sqrt2`$, forcing $`\gamma=\pi/4\pmod{\pi/2}`$. Hence (8) still holds. This exact observation does not extend the finite-error theorem to arbitrary non-diagonal endpoint rotations.

## 10. Direct converse for the vacuum lossy channel

Assume the [vacuum Markov model](loss_and_frontier.md): every mode and its input field starts in vacuum, the common number-decay rate is $`\kappa\ge0`$, and the actual damped displacement matrix $`D(t)\in\mathbb C^{m\times2K}`$ obeys

```math
\dot D=u-\kappa D/2,\qquad D(0)=D(T)=0,\qquad
A=\mathrm{Im}\int_0^TD^\dagger\dot D\,dt,\qquad
F+iJ=\int_0^TD^\dagger D\,dt.
```

Use the same independently controlled complex forces and commuting qubit axes as before. The [exact channel derivation](loss_and_frontier.md#1-exact-channel-including-the-imaginary-trajectory-gram-matrix) gives coherence multiplier

```math
\lambda_{zr}=\exp\left[-\frac\kappa2(z-r)^{\mathsf T}F(z-r)\right]
\exp i\left[z^{\mathsf T}Az-r^{\mathsf T}Ar+\kappa r^{\mathsf T}Jz\right].
\qquad\text{(29)}
```

The imaginary Gram term generally cannot be discarded or represented by one diagonal unitary.

**Noisy phase-extraction theorem.** If this actual channel has half-diamond distance at most $`\epsilon<1/(2\sqrt2)`$ from a locally $`Z`$-dressed matching, then the cross-block statement (14), the weighted estimate (19), and the finite-size estimates (27) hold with

```math
\delta=\arcsin(2\epsilon),\qquad \eta=4\delta/\pi.
\qquad\text{(30)}
```

Their energy is the derivative fluence $`E_{\rm path}=\int\lVert\dot D\rVert_F^2dt`$. The physical paid fluence is

```math
\mathcal E=\int\lVert u\rVert_F^2dt
=E_{\rm path}+\frac{\kappa^2}{4}X\ge E_{\rm path},\qquad
X=\mathrm{tr}F.
\qquad\text{(31)}
```

Thus (3), (4), (23), (24), and (27) remain valid as necessary bounds on the paid action and force-limited duration, with the substitution (30). No premise that the ideal area unitary itself approximates the target is needed.

**Proof.** Fix one reference string $`r`$. Input $`(|z\rangle+|r\rangle)/\sqrt2`$ for each $`z\ne r`$. If the target coherence multiplier is $`v_zv_r^*`$, half-trace distance of these two outputs is $`|\lambda_{zr}-v_zv_r^*|/2`$. The channel assumption therefore gives

```math
|\lambda_{zr}-v_zv_r^*|\le2\epsilon.
```

After division by the target phase the actual multiplier is $`a e^{i\phi}`$, with $`0\le a\le1`$. The disk $`|ae^{i\phi}-1|\le2\epsilon<1`$ confines its angle modulo $`2\pi`$ to $`[-\arcsin(2\epsilon),\arcsin(2\epsilon)]`$; the extremal ray is tangent to that disk. For fixed $`r`$, the bath phase $`\kappa r^{\mathsf T}Jz`$ is linear in $`z`$. Hence the phase relative to the target is a quadratic Boolean polynomial with exactly the geometric cross-block coefficients. The third-difference argument of Section 4 applies since $`\delta<\pi/4`$, then its Parseval estimate gives $`\lVert R\rVert_F\le\delta/2`$. The rest of the spectral and perturbation proof is unchanged. Finally, expanding $`\lVert\dot D+\kappa D/2\rVert_F^2`$ gives (31): its integrated cross term is $`(\kappa/2)[\lVert D(T)\rVert_F^2-\lVert D(0)\rVert_F^2]=0`$. $`\square`$

The reference-dependent linear term is a proof device; it does not assert that one physical local correction removes every bath coherence phase simultaneously. Exact damped closure remains a hypothesis. These are necessary bounds, with no claim of a noisy construction achieving the requested error or an exact diamond-error frontier. A separate [loss-induced duration constraint](hardware_resources.md#8-a-global-accuracy-constraint-from-vacuum-loss) follows from the exposure floor and can be combined with this finite-mode converse.

## References

1. J. Haah, R. Kothari, R. O'Donnell, and E. Tang, *Query-optimal estimation of unitary channels in diamond distance*, FOCS 2023, pp. 363–390; [arXiv:2302.14066](https://arxiv.org/abs/2302.14066), [author manuscript, Appendix A](https://www.cs.cmu.edu/~odonnell/papers/estimating-unitaries.pdf), [DOI:10.1109/FOCS57990.2023.00028](https://doi.org/10.1109/FOCS57990.2023.00028). The half-diamond convention and numerical-range relation used in Section 3 agree with Definition 1.3 and the proof of Proposition 1.6 in that manuscript.
2. L. Mirsky, *Symmetric gauge functions and unitarily invariant norms*, Quarterly Journal of Mathematics **11** (1960), 50–59, [DOI:10.1093/qmath/11.1.50](https://doi.org/10.1093/qmath/11.1.50). Section 5 supplies the special Frobenius perturbation argument used here.
