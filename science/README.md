# Scientific reading map

The question is whether a fixed number of harmonic mediators can sustain an extensive layer of independent two-qubit gates at bounded coupling strength. The answer depends on the number of independent phase directions, the quantum gate's phase equivalences, and what is paid to return the bus.

## Connected route

1. **[Model and conventions](model.md).** Fix the commuting spin-dependent Hamiltonian, exact conditional closure, geometric matrix $`K`$, and resources $`E`$, $`G`$ and $`X`$. A physical pair angle is $`2K_{ij}`$; ordinary diagonal entries of $`K`$ are global phase.
2. **[Spectral control cost](spectral_cost.md).** Resolve a closed path into signed temporal harmonics. Each carries at most $`2b`$ real phase directions. A rank-tail argument gives the exact fixed-matrix optimum and a sharp bound for a cross block.
3. **[Matching gates and robustness](matching.md).** A CZ matching has cross block $`(\pi/8)(I+2B)`$ for an integer matrix $`B`$. Its odd determinant prevents phase wrapping from removing the cost. A Boolean unwrapping lemma and singular-value stability extend the result to fixed gate error, including the actual lossy channel.
4. **[Loss and the exposure frontier](loss_and_frontier.md).** Derive the exact emitted-field channel, including its skew phase, then solve the damping- and exposure-priced control problem. Separate an exact scalar resource frontier from a full gate-error optimum.
5. **[Architecture and examples](architecture.md).** Translate the bounds into per-qubit drive requirements, compare few- and many-mode designs, and charge modulation, occupation, preparation and memory.

## Claims and dependencies

| Claim | Required inputs | Proof home |
|---|---|---|
| $`E_{\min}T=2\pi\Phi_b(K)`$ | Closed $`H^1`$ trajectories; independent complex couplings | Spectral cost, Theorem SC1 |
| Sharp cross-block cost | Signed eigenvalue tails; nuclear-norm rank approximation | Spectral cost, Theorem SC2 |
| $`E^*_{m,b}(T)T=\Theta(m+m^2/b)`$ for the optimal lossless CZ matching | Exact phase lift; odd determinant; spectral converse; explicit pulses | Matching, Lemma M1, Theorem M2 and constructions |
| Fixed-error congestion | Quadratic Boolean rounding; Parseval; singular-value perturbation | Matching, Lemma M3 and Theorem M4 |
| Direct noisy-gate converse | Vacuum Markov coherent-state dilation; one-reference phase extraction | Matching, Theorem M5 |
| Exact $`(G,X)`$ frontier for fixed $`K`$ | Complete compact area spectrum with a mass term; weighted rank allocation | Loss/frontier, equations L13–L22 |
| Global loss-induced duration constraint | Robust nuclear lower bound; target-independent exposure floor; paid drive cap | Architecture, section 2 |

## Scientific distinctions to retain

- A physical bus mode and a temporal control harmonic are different resources.
- The positive and negative spectra are ordered separately; a signed harmonic has real multiplicity $`2b`$.
- A fixed-matrix optimum does not already optimize over a quantum gate's phase representatives.
- The lossless constructive matching bounds and the noisy necessary bounds have different attainability claims.
- $`E`$ is derivative action. The paid damped force action is $`G=E+\kappa^2X/4`$.
- $`X`$ is integrated basis-averaged displacement occupation. It is neither the full error channel nor a maximum-branch occupation bound.
- The imaginary environmental Gram matrix must be retained in the exact channel.

The [source comparison](../references/related_work.md) identifies the inherited control and dissipative ingredients. The [verification guide](../verification/README.md) maps finite computations to the analytical claims they support. The [repository entrypoint](../README.md) gives the main results without proof details.
