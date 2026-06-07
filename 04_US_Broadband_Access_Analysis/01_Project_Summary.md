# County-Level Broadband Access in the United States — Summary

## The problem

By national headlines, broadband looks like a mostly solved problem: most
Americans have it. But national and state averages blur over enormous local
variation, and they say nothing about *why* some places are left behind. This
project uses public county-level data for 3,102 U.S. counties to ask two
practical questions: where is broadband adoption actually lowest, and what
predicts it — the infrastructure that's available, or the economic conditions of
the households who would have to pay for it?

## What the data show

**The gap that averages hide is large.** The share of households with home
broadband ranges from 25.7% to 95.5% across counties, with a median of 73.7%.
The bottom 5% of counties are below 56%. A single national number averages a
well-connected county with one where a quarter of homes have no broadband at all.

**Economic conditions predict adoption better than infrastructure does.** This is
the central finding. Comparing each factor's correlation with actual
home-broadband adoption, poverty is the strongest single predictor (r = -0.65),
with the share of households receiving SNAP close behind (r = -0.57). Formal
broadband availability — whether providers nominally serve the county —
correlates only weakly (r = +0.30), and raw provider count weaker still
(r = +0.22). In other words, the signal that points to where households are
offline is mostly about affordability and need, not about whether wires reach the
county.

![Poverty correlates with adoption more than infrastructure does](docs/figures/fig03-adoption-correlates.png)

**Availability is not adoption.** Among the 1,044 counties with formal
availability at or above 90% — counties a coverage map would call "served" —
mean household adoption is still only 76.1%, and the lowest is 39%. Counting
where providers exist substantially overstates where households are actually
connected.

**The gap maps onto economic disadvantage and geography.** Sorting counties into
poverty quartiles, adoption falls 15 points from 79.2% in the lowest-poverty
quartile to 64.3% in the highest. The same pattern shows up geographically: the
South averages 69.2% county adoption versus 79.2% in the Northeast, and the
lowest-adoption states — Mississippi (61.1%), New Mexico (63.2%), Arkansas
(64.2%) — sit in the Deep South and rural Southwest where poverty is highest.

![Adoption falls across poverty quartiles](docs/figures/fig05-poverty-quartile.png)

## What it means

If the goal is to close the broadband gap, these patterns point to where effort
pays off. Because adoption tracks poverty more than coverage, programs that only
fund infrastructure buildout in nominally underserved areas will miss the larger
problem: high-poverty counties where service exists but households can't afford or
don't adopt it. Targeting affordability support and adoption assistance in
economically disadvantaged counties — concentrated in the South and rural
Southwest — is where the data suggest the divide is widest. These are descriptive
patterns from observational, multi-year data, so they are best used to target and
prioritize rather than as causal or current-condition claims.

An interactive Tableau version of the geographic story is available on
[Tableau Public](https://public.tableau.com/app/profile/mintay/viz/DVProject1-Tableau-AmericasBroadbandProblem/AmericasBroadbandProblem).
