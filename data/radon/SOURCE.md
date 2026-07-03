# Minnesota radon data (Gelman & Hill multilevel example)

Radon measurements from 919 owner-occupied homes across 85 Minnesota counties.
The canonical dataset for mixed-effects / multilevel regression.

- `log_radon`: log radon concentration (the response).
- `floor`: 0 = basement, 1 = first floor (measurement level).
- `county`: Minnesota county (the grouping factor).
- `Uppm`: county soil-uranium level (a county-level predictor).

Source: Gelman, A. and Hill, J. (2007), *Data Analysis Using Regression and
Multilevel/Hierarchical Models*. Cleaned from the pymc-devs mirror of Gelman's
radon example (http://www.stat.columbia.edu/~gelman/arm/examples/radon/).
