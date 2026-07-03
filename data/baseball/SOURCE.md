# Efron-Morris 1975 baseball batting data

Batting averages for 18 major-league baseball players through their first 45
at-bats of the 1970 season, with their batting average over the remainder of the
season. The canonical dataset for James-Stein / hierarchical-Bayes shrinkage.

- `hits_45`, `avg_45`: hits and average in the first 45 at-bats.
- `remaining_ab`, `remaining_avg`: at-bats and average for the rest of the season
  (the held-out target the early sample is used to predict).

Source: Efron, B. and Morris, C. (1975), "Data Analysis Using Stein's Estimator
and Its Generalizations," JASA 70(350):311-319. Retrieved via the Rdatasets
mirror of the R `pscl` package (`EfronMorris`).
