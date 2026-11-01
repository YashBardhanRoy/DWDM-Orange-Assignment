#!/usr/bin/env python3
"""Build reproducible Adult Income CSV inputs and summaries for the Orange practicals.

Run from any directory with Python 3: python prepare_adult_exports.py
The source file is datasets/adult.data from the UCI Adult dataset. These files are
prepared inputs/summaries; they are not exported Orange model predictions.
"""
from collections import Counter, defaultdict
import csv
import math
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "adult.data"
FIELDS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country", "income",
]
NUMERIC = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
MISSING_CATEGORICAL = ["workclass", "occupation", "native_country"]


def read_source():
    with SOURCE.open("r", encoding="utf-8", newline="") as handle:
        rows = [[value.strip() for value in row] for row in csv.reader(handle, skipinitialspace=True) if row]
    bad = [i + 1 for i, row in enumerate(rows) if len(row) != len(FIELDS)]
    if bad:
        raise ValueError(f"Expected {len(FIELDS)} columns; invalid rows: {bad[:5]}")
    return rows


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(fields)
        writer.writerows(rows)


def nice(value):
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.6f}".rstrip("0").rstrip(".") if value else "0"
    return str(value)


def make_cuts(values, bins=5):
    ordered = sorted(values)
    cuts = []
    for i in range(1, bins):
        index = min(len(ordered) - 1, math.ceil(i * len(ordered) / bins) - 1)
        cut = ordered[index]
        if not cuts or cut > cuts[-1]:
            cuts.append(cut)
    return cuts


def quantile_label(value, cuts):
    for index, cut in enumerate(cuts, start=1):
        if value <= cut:
            return f"Q{index}"
    return f"Q{len(cuts) + 1}"


def main():
    raw_rows = read_source()
    index = {name: FIELDS.index(name) for name in FIELDS}
    modes = {}
    for name in MISSING_CATEGORICAL:
        values = [row[index[name]] for row in raw_rows if row[index[name]] != "?"]
        modes[name] = Counter(values).most_common(1)[0][0]

    # Keep ? in the raw task input so Orange recognizes missing values.
    write_csv(ROOT / "01_data_cleaning" / "data_cleaning_missing_values.csv", FIELDS, raw_rows)
    clean_rows = []
    for row in raw_rows:
        clean = row.copy()
        for name, replacement in modes.items():
            if clean[index[name]] == "?":
                clean[index[name]] = replacement
        clean_rows.append(clean)
    write_csv(ROOT / "01_data_cleaning" / "output_cleaned_imputed.csv", FIELDS, clean_rows)

    # Data reduction: retain the four predictors and income target described in the report.
    reduced_fields = ["age", "education_num", "sex", "hours_per_week", "income"]
    write_csv(ROOT / "02_data_reduction" / "output_reduced.csv", reduced_fields,
              [[row[index[name]] for name in reduced_fields] for row in clean_rows])

    numeric_values = {name: [float(row[index[name]]) for row in clean_rows] for name in NUMERIC}
    bounds = {name: (min(vals), max(vals)) for name, vals in numeric_values.items()}
    normalized_rows = []
    for row in clean_rows:
        out = row.copy()
        for name in NUMERIC:
            lo, hi = bounds[name]
            val = float(row[index[name]])
            out[index[name]] = nice((val - lo) / (hi - lo)) if hi != lo else "0"
        normalized_rows.append(out)
    write_csv(ROOT / "03_data_transformation" / "output_normalized_0_1.csv", FIELDS, normalized_rows)

    # Apriori transaction input: categorical value items plus equal-frequency bins for numeric fields.
    cuts = {name: make_cuts(vals) for name, vals in numeric_values.items()}
    category_fields = ["workclass", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "income"]
    transaction_rows = []
    for record_id, row in enumerate(clean_rows, start=1):
        items = [f"{name}={row[index[name]]}" for name in category_fields]
        items += [f"{name}={quantile_label(float(row[index[name]]), cuts[name])}" for name in NUMERIC]
        transaction_rows.append([record_id, ";".join(items)])
    write_csv(ROOT / "04_association_rules_apriori" / "transactions.csv", ["record_id", "items"], transaction_rows)

    # Descriptive feature statistics and class-wise comparison summaries.
    stat_fields = ["feature", "type", "count", "missing_count", "mean", "median", "min", "max", "mode", "mode_count"]
    stats_rows = []
    for name in FIELDS:
        col = [row[index[name]] for row in raw_rows]
        valid = [v for v in col if v != "?"]
        mode, mode_count = Counter(valid).most_common(1)[0]
        if name in NUMERIC:
            vals = [float(v) for v in valid]
            stats_rows.append([name, "numeric", len(valid), len(col) - len(valid),
                               nice(statistics.mean(vals)), nice(statistics.median(vals)),
                               nice(min(vals)), nice(max(vals)), nice(mode), mode_count])
        else:
            stats_rows.append([name, "categorical", len(valid), len(col) - len(valid), "", "", "", "", mode, mode_count])
    write_csv(ROOT / "05_statistical_analysis" / "adult_feature_statistics.csv", stat_fields, stats_rows)

    classes = defaultdict(list)
    for row in clean_rows:
        classes[row[index["income"]]].append(row)
    class_fields = ["income", "count", "age_mean", "age_median", "education_num_mean", "education_num_median", "hours_per_week_mean", "hours_per_week_median"]
    class_rows = []
    for label in sorted(classes):
        group = classes[label]
        vals = {name: [float(r[index[name]]) for r in group] for name in ["age", "education_num", "hours_per_week"]}
        class_rows.append([label, len(group)] + [nice(x) for name in ["age", "education_num", "hours_per_week"]
            for x in (statistics.mean(vals[name]), statistics.median(vals[name]))])
    write_csv(ROOT / "05_statistical_analysis" / "income_class_summary.csv", class_fields, class_rows)

    # Experiment inputs. Clusters/outlier labels are deliberately not invented.
    regression_fields = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
    write_csv(ROOT / "06_regression" / "adult_regression_input.csv", regression_fields,
              [[row[index[name]] for name in regression_fields] for row in clean_rows])
    write_csv(ROOT / "07_outlier_analysis" / "adult_outlier_input.csv", NUMERIC,
              [[row[index[name]] for name in NUMERIC] for row in clean_rows])
    kmeans_fields = NUMERIC
    normalized_numeric = [[row[index[name]] for name in kmeans_fields] for row in normalized_rows]
    write_csv(ROOT / "08_kmeans_adult" / "adult_kmeans_input.csv", kmeans_fields, normalized_numeric)
    write_csv(ROOT / "09_clustering_adult_simple" / "adult_simple_kmeans_input.csv", kmeans_fields, normalized_numeric)

    print(f"rows={len(raw_rows)}; modes={modes}; files=11")


if __name__ == "__main__":
    main()
