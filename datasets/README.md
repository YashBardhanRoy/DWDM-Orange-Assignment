# Adult Income datasets

## Source

This repository uses the 32,561-record Adult Census Income training file from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult), cited as Becker and Kohavi (1996), DOI [10.24432/C5XW20](https://doi.org/10.24432/C5XW20). The data are distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); retain attribution when reusing them.

- [adult.data](adult.data) is the shared source file.
- [adult.names](adult.names) contains the attribute description.
- [prepare_adult_exports.py](prepare_adult_exports.py) regenerates the practical CSV files with Python 3 and the standard library.

## Practical files

| Folder | Files |
|---|---|
| [01_data_cleaning/](01_data_cleaning/) | Missing-value input and categorical-mode imputation output |
| [02_data_reduction/](02_data_reduction/) | Reduced five-column dataset |
| [03_data_transformation/](03_data_transformation/) | Numeric attributes normalized to [0, 1] |
| [04_association_rules_apriori/](04_association_rules_apriori/) | Apriori transaction input with categorical items and numeric bins |
| [05_statistical_analysis/](05_statistical_analysis/) | Feature statistics and income-class summary |
| [06_regression/](06_regression/) | Numeric regression input |
| [07_outlier_analysis/](07_outlier_analysis/) | Numeric outlier-analysis input |
| [08_kmeans_adult/](08_kmeans_adult/) | Normalized numeric K-Means input |
| [09_clustering_adult_simple/](09_clustering_adult_simple/) | Normalized numeric clustering input |

The CSVs in the practical folders are reproducible inputs or descriptive summaries derived from adult.data. They are not original Orange table exports or saved Orange model outputs. The report screenshots document the Orange settings and reported outcomes; no cluster assignments, outlier labels, or model predictions have been fabricated. The original DOCX is intentionally omitted.
