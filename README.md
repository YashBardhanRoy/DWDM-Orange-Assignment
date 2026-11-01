# DWDM Orange Assignment — Adult Census Income

Data Warehousing and Data Mining practicals completed with Orange Data Mining, using the Adult Census Income dataset. The repository follows the reference assignment's experiment-by-experiment layout, with the Adult Income topic, dataset notes, and screenshots from the supplied report.

> The original DOCX is not included. Individual Orange screenshots are included; full-page report renders are omitted because the source report contains personal student details.

## Dataset

The assignment uses 32,561 records from the UCI Adult dataset. The data and attribute description are in [`datasets/`](datasets/). Source: [UCI Machine Learning Repository — Adult](https://archive.ics.uci.edu/dataset/2/adult); Becker and Kohavi (1996), DOI [10.24432/C5XW20](https://doi.org/10.24432/C5XW20). Dataset license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Dataset preview

![Adult data preview](screenshots/00_dataset_preview/adult_data_preview.png)

### Dataset files

The numbered folders in [`datasets/`](datasets/) contain CSV inputs and summaries for the nine practicals, including the missing-value input, cleaned and reduced data, normalized data, Apriori transactions, and statistical summaries. [`datasets/prepare_adult_exports.py`](datasets/prepare_adult_exports.py) regenerates these files. They are derived from the Adult source and are clearly documented as prepared data, not original Orange output exports.

## Experiments

| # | Practical | Main result | Details | Screenshots |
|---|---|---|---|---|
| 01 | Data Cleaning | Missing values in workclass, occupation, and native-country were imputed; the cleaned preview shows no missing values. | [Dataset notes](datasets/01_data_cleaning/README.md) | [Images](screenshots/01_data_cleaning/) |
| 02 | Data Reduction | Selected age, education-num, sex, and hours-per-week as predictors, with income as target. | [Dataset notes](datasets/02_data_reduction/README.md) | [Images](screenshots/02_data_reduction/) |
| 03 | Data Transformation | Normalized numeric attributes to [0, 1]. | [Dataset notes](datasets/03_data_transformation/README.md) | [Images](screenshots/03_data_transformation/) |
| 04 | Association Rules — Apriori | The report records 110 itemsets and 113 rules. The top reported rule has 0.993 confidence and 2.45 lift. | [Dataset notes](datasets/04_association_rules_apriori/README.md) | [Images](screenshots/04_association_rules_apriori/) |
| 05 | Statistical Analysis | Age mean 38.58; median age by income class: 34 (≤50K) and 44 (>50K). | [Dataset notes](datasets/05_statistical_analysis/README.md) | [Images](screenshots/05_statistical_analysis/) |
| 06 | Regression | Linear Regression was best in the report comparison (RMSE 11.204, MAE 7.770, R² 0.177). | [Dataset notes](datasets/06_regression/README.md) | [Images](screenshots/06_regression/) |
| 07 | Outlier Analysis | A 10% contamination setting flagged 3,256 records. | [Dataset notes](datasets/07_outlier_analysis/README.md) | [Images](screenshots/07_outlier_analysis/) |
| 08 | K-Means on Adult Income | k=3; reported cluster sizes 14,394, 9,152, and 9,015; silhouette 0.278. | [Dataset notes](datasets/08_kmeans_adult/README.md) | [Images](screenshots/08_kmeans_adult/) |
| 09 | Simple K-Means Clustering | k=2; 11,414 records (35.05%) were mismatched in the class-to-cluster comparison. | [Dataset notes](datasets/09_clustering_adult_simple/README.md) | [Images](screenshots/09_clustering_adult_simple/) |

## Repository structure

```text
DWDM-Orange-Assignment/
├── README.md
├── datasets/
│   ├── adult.data
│   ├── adult.names
│   ├── README.md
│   └── 01_data_cleaning/ ... 09_clustering_adult_simple/
└── screenshots/
    ├── 00_dataset_preview/
    ├── 01_data_cleaning/ ... 09_clustering_adult_simple/
    └── full_pdf_pages/ (privacy note)
```

## Screenshots

The images below are exported from the supplied report. Each numbered folder contains the matching workflow, configuration, and result views.

### 01. Data Cleaning

Missing values in workclass, occupation, and native-country were imputed; the cleaned preview shows no missing values.

**Orange workflow**

![Orange workflow](screenshots/01_data_cleaning/orange_workflow.png)

**Impute settings**

![Impute settings](screenshots/01_data_cleaning/impute_settings.png)

**Cleaned data preview**

![Cleaned data preview](screenshots/01_data_cleaning/cleaned_data_preview.png)

### 02. Data Reduction

Selected age, education-num, sex, and hours-per-week as predictors, with income as target.

**Orange workflow**

![Orange workflow](screenshots/02_data_reduction/orange_workflow.png)

**Select Columns settings**

![Select Columns settings](screenshots/02_data_reduction/select_columns_settings.png)

**Reduced data preview**

![Reduced data preview](screenshots/02_data_reduction/reduced_data_preview.png)

### 03. Data Transformation

Normalized numeric attributes to [0, 1].

**Orange workflow**

![Orange workflow](screenshots/03_data_transformation/orange_workflow.png)

**Normalize settings**

![Normalize settings](screenshots/03_data_transformation/normalize_settings.png)

**Before normalization**

![Before normalization](screenshots/03_data_transformation/before_normalization.png)

**Normalized data preview**

![Normalized data preview](screenshots/03_data_transformation/normalized_data_preview.png)

### 04. Association Rules — Apriori

The report records 110 itemsets and 113 rules. The top reported rule has 0.993 confidence and 2.45 lift.

**Orange workflow**

![Orange workflow](screenshots/04_association_rules_apriori/orange_workflow.png)

**Apriori settings**

![Apriori settings](screenshots/04_association_rules_apriori/apriori_settings.png)

**Association rule output**

![Association rule output](screenshots/04_association_rules_apriori/association_rules.png)

### 05. Statistical Analysis

Age mean 38.58; median age by income class: 34 (≤50K) and 44 (>50K).

**Orange workflow**

![Orange workflow](screenshots/05_statistical_analysis/orange_workflow.png)

**Feature statistics**

![Feature statistics](screenshots/05_statistical_analysis/feature_statistics.png)

**Education distribution by income**

![Education distribution by income](screenshots/05_statistical_analysis/education_by_income_distribution.png)

**Age box plot by income**

![Age box plot by income](screenshots/05_statistical_analysis/age_boxplot_by_income.png)

### 06. Regression

Linear Regression was best in the report comparison (RMSE 11.204, MAE 7.770, R² 0.177).

**Orange workflow**

![Orange workflow](screenshots/06_regression/orange_workflow.png)

**Target configuration**

![Target configuration](screenshots/06_regression/target_configuration.png)

**Linear Regression settings**

![Linear Regression settings](screenshots/06_regression/linear_regression_settings.png)

**Test and Score**

![Test and Score](screenshots/06_regression/test_and_score.png)

### 07. Outlier Analysis

A 10% contamination setting flagged 3,256 records.

**Orange workflow**

![Orange workflow](screenshots/07_outlier_analysis/orange_workflow.png)

**Outlier settings**

![Outlier settings](screenshots/07_outlier_analysis/outlier_settings.png)

**Outlier scatter plot**

![Outlier scatter plot](screenshots/07_outlier_analysis/outlier_scatter_plot.png)

**Outlier data preview**

![Outlier data preview](screenshots/07_outlier_analysis/outlier_data_preview.png)

### 08. K-Means on Adult Income

k=3; reported cluster sizes 14,394, 9,152, and 9,015; silhouette 0.278.

**Orange workflow**

![Orange workflow](screenshots/08_kmeans_adult/orange_workflow.png)

**K-Means settings**

![K-Means settings](screenshots/08_kmeans_adult/kmeans_settings.png)

**Clusters scatter plot**

![Clusters scatter plot](screenshots/08_kmeans_adult/clusters_scatter_plot.png)

**Clustered data preview**

![Clustered data preview](screenshots/08_kmeans_adult/clustered_data_preview.png)

### 09. Simple K-Means Clustering

k=2; 11,414 records (35.05%) were mismatched in the class-to-cluster comparison.

**Orange workflow**

![Orange workflow](screenshots/09_clustering_adult_simple/orange_workflow.png)

**K-Means settings**

![K-Means settings](screenshots/09_clustering_adult_simple/kmeans_settings.png)

**Cluster centroids**

![Cluster centroids](screenshots/09_clustering_adult_simple/cluster_centroids.png)

**Classes to clusters**

![Classes to clusters](screenshots/09_clustering_adult_simple/classes_to_clusters.png)

## Notes

- `datasets/adult.data` is the shared source; each experiment folder contains its corresponding Adult CSV input or summary plus a short explanation.
- Numeric preprocessing and experiment settings are documented in the corresponding dataset README and shown in the screenshots.
- No Orange workflow (`.ows`) files or exported analysis tables were included in the source document; the included CSVs are reproducible inputs and summaries prepared from the shared Adult data.
- `screenshots/full_pdf_pages/README.md` explains why full-page report images are omitted.
