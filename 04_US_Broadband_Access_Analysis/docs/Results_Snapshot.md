# Results Snapshot

Verified values from `04_Source_Code.py` over 3,102 counties (public IMLS /
BroadbandNow extract).

## Outcome distribution — home broadband adoption

| Statistic | Value |
|---|---|
| Median | 73.7% |
| 5th–95th percentile | 55.8% – 86.5% |
| Full range | 25.7% – 95.5% (69.8 pts) |

## Correlation with adoption (Pearson r)

| Factor | r |
|---|---:|
| Poverty rate | -0.65 |
| SNAP receipt | -0.57 |
| Avg download speed | +0.46 |
| No health insurance | -0.41 |
| Unemployment | -0.38 |
| Formal availability | +0.30 |
| Provider count | +0.22 |
| Monthly cost | +0.04 |

Poverty |r| (0.65) is more than double formal availability |r| (0.30).

## Adoption by poverty quartile

| Quartile | Mean adoption |
|---|---:|
| Q1 (lowest poverty) | 79.2% |
| Q2 | 75.6% |
| Q3 | 71.8% |
| Q4 (highest poverty) | 64.3% |

Q1 vs Q4 gap: 15.0 points.

## Availability is not adoption

1,044 counties have formal availability ≥ 90%; their mean household adoption is
only 76.1%, with a low of 39.0%.

## Regional and state extremes

| Region | Mean adoption (n) |
|---|---|
| Northeast | 79.2% (217) |
| West | 76.8% (445) |
| Midwest | 74.4% (1,050) |
| South | 69.2% (1,390) |

Lowest states: Mississippi 61.1%, New Mexico 63.2%, Arkansas 64.2%.
Highest states: Connecticut 84.1%, Rhode Island 83.9%, Massachusetts 83.8%.

## Figures (`docs/figures/`)

`fig01-broadband-distribution.png`, `fig02-poverty-vs-broadband.png`,
`fig03-adoption-correlates.png`, `fig04-state-ranking.png`,
`fig05-poverty-quartile.png`, `fig06-availability-vs-adoption.png`,
`fig07-region.png`.
