# Learning route: quantum bus congestion

This folder connects the physical idea of a trapped-ion geometric gate to the project's question: how do the number of harmonic bus modes, the coupling available to each qubit, gate time, and global channel accuracy constrain a layer of independent CZ gates?

The selected educational anchor is **Häffner, Roos and Blatt, *Quantum computing with trapped ions* (2008)**, specifically the [arXiv:0809.4368v1 preprint](https://arxiv.org/pdf/0809.4368v1). This is one foundations anchor, with selected sections rather than a requirement to read the entire review. Its experimental numbers provide historical context; the project's current source comparisons are in [Related work](../references/related_work.md).

## The two learning documents

| Document | Purpose |
|---|---|
| [Häffner bridge](HAEFFNER_BRIDGE.md) | Verified preprint section/page pointers, notation translation, a complete paid single-CZ example, and the connections to rank allocation, phase equivalence, robustness, and loss. |
| [30-milestone map](MILESTONES.md) | The complete dependency map: **M01–M13** build the background; **M14–M30** develop the scientific narrative. |

The bridge explains why the physical ingredients lead to the mathematical objects. The map identifies how those ingredients assemble into the whole result. Neither replaces the exact theorem statements.

## Connections to the scientific pages

| Part of the question | Milestones | Scientific account |
|---|---|---|
| A conditional loop, the chosen gate, and the paid resources | M01–M15 | [Model](../science/model.md) |
| Phase/exposure inequalities and finite-bus temporal capacity | M16–M19 | [Spectral cost](../science/spectral_cost.md) |
| CZ phase representatives and robust matching bounds | M20–M24 | [Matching theorem](../science/matching.md) |
| Exact vacuum-loss channel and the force–exposure frontier | M25–M28 | [Loss and frontier](../science/loss_and_frontier.md) |
| Architecture comparisons and the complete scope | M29–M30 | [Architecture](../science/architecture.md) |

The main distinctions remain visible throughout: a physical oscillator mode is different from a temporal harmonic; laser parameters require a calibration to the model's force bound; a fixed phase matrix is different from a gate-equivalence class; vacuum damping is different from motional heating; and an exact exposure frontier is different from an exact channel-error frontier.

[The verification guide](../verification/README.md) records finite checks of the analytical formulas. [The source comparison](../references/related_work.md) attributes the inherited geometric-control and dissipative ingredients. Those research references support the argument without adding another educational anchor.
