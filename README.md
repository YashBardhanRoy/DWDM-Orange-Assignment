# DWDM Orange Assignment

Practical work for Data Warehousing and Data Mining using Orange Data Mining. The report covers nine experiments on the Adult Census Income dataset.

## Experiments

1. **Data cleaning** — impute missing numeric values with the mean and categorical values with the mode.
2. **Data reduction** — retain age, education-num, sex, and hours-per-week as features, with income as the target.
3. **Data transformation** — normalize numeric attributes to the range [0, 1].
4. **Association rules** — apply Apriori with 30% minimum support and 85% minimum confidence; the report records 110 frequent itemsets and 113 rules.
5. **Statistical analysis** — inspect descriptive statistics and compare age and education distributions by income class.
6. **Regression** — predict hours-per-week with 10-fold cross-validation; linear regression has the lowest reported RMSE (11.204).
7. **Outlier analysis** — use a covariance estimator with 10% contamination; 3,256 rows are flagged.
8. **K-means clustering** — cluster six normalized numeric attributes into three groups; reported silhouette score is 0.278.
9. **Simple K-means** — compare two clusters against the income classes; the report records 35.05% incorrectly clustered instances.

## Dataset

The report identifies `adult.data` from the Adult Census Income dataset as the input for all nine experiments. It contains 32,561 records and 14 attributes plus the income class. Missing values are marked in workclass, occupation, and native-country.

The experiment descriptions and results are summarized from the provided assignment document. The original document and its embedded screenshots are not included in this repository yet.
