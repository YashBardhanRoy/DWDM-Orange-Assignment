# Experiment 1 — Data Cleaning

**Input:** [`data_cleaning_missing_values.csv`](data_cleaning_missing_values.csv), the shared Adult source with `?` retained as the missing-value marker.

**Prepared output:** [`output_cleaned_imputed.csv`](output_cleaned_imputed.csv). Missing categorical values in `workclass`, `occupation`, and `native_country` are filled with each column's most frequent observed category (`Private`, `Prof-specialty`, `United-States`). Numeric values are unchanged. The source counts and Orange method are described in the screenshots.

This is a reproducible CSV preparation based on the source data; it is not an Orange widget export.

Screenshots: [`../../screenshots/01_data_cleaning/`](../../screenshots/01_data_cleaning/).
