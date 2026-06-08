# Summary: Matching the Test to the Question

Comparing group averages sounds simple, but the "right" way to do it depends entirely on how the data were collected: one group or several, measured once or repeatedly, one factor or two interacting. This project walks through four real research questions and uses the analysis-of-variance (ANOVA) design each one actually calls for. The point is practical — the wrong design doesn't just lose precision, it can hide or reverse the answer.

## The four findings

**1. More training, less willingness.** Three groups received different intensities of cross-cultural communication training, then rated how much more they'd want to talk across cultures. Counter to expectation, the control group scored highest and the high-intensity group lowest, and the difference was real and large (η² = .19, meaning about a fifth of the variation in willingness lines up with training group). When the three groups are compared head-to-head, only the high-intensity-vs-control gap is statistically reliable — a useful caution that a significant overall test does not mean every pair differs.

**2. Bias that only shows up in context.** At pedestrian crosswalks, whether drivers yielded did *not* differ overall by the pedestrian's race. But it differed sharply once neighborhood income was added. In lower-income blocks, more cars failed to yield to the Black pedestrian; in higher-income blocks the pattern flipped. This is an *interaction* — the effect of one factor depends on the level of another — and it is the entire story. A test that looked only at race would have reported "no bias" and been wrong.

![Driver non-yielding by pedestrian race across neighborhood income levels; the two lines cross, showing the racial gap reverses by income](docs/figures/factorial-lineplot-1.png)

**3. Gains that stick.** A resilience program measured the same 50 people three times: before, right after, and six months later. Resilience rose significantly from before to after, and — importantly — did not slip back at the six-month follow-up. Because the same people are tracked over time, this design filters out stable personal differences and detects change with far fewer participants than separate groups would need.

**4. Slow separation, not instant effect.** Three groups (no training, skills only, skills plus contact) were tracked across the same three time points on their group-exclusion attitudes. At the start the groups were statistically indistinguishable — exactly what random assignment should produce — and they only pulled apart by the six-month follow-up. By then both trained groups differed from the control group, but the two trained groups did *not* differ reliably from each other: adding contact on top of skills did not produce a detectable extra benefit in this data.

![Exclusion-attitude trajectories by training condition over three waves; groups start together and diverge by follow-up](docs/figures/mixed-lineplot-1.png)

## The takeaway

Each design answers a question the others can't. A one-way test compares independent groups; a factorial test reveals when two factors combine; a repeated-measures test tracks change in the same people with high power; a mixed design does both at once and is the standard for "did the program work over time" questions. The discipline is identical across all four: check the assumptions, run the overall test, follow up only where it's warranted, correct for multiple comparisons, and report effect sizes so a reader can judge whether a result matters and not just whether it's significant. Read **[02_Project_Report.md](./02_Project_Report.md)** for the full technical treatment.

*All four datasets are simulated from published population parameters, so the results are reproducible and the data are fully shareable.*
