import pandas as pd
import glob
import os

files = sorted(
    glob.glob(
        r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\datasets\raw_dataset.csv\test_result_2024*.csv"
    )
)

output_file = r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\datasets\cleaned_2024_final.csv"

first_file = True

for file in files:
    print("Processing:", os.path.basename(file))

    df = pd.read_csv(file, escapechar="\\", low_memory=False)

    df = df[df["test_date"] != "test_date"]
    df = df.drop_duplicates()

    df["test_date"] = pd.to_datetime(df["test_date"], errors="coerce")
    df["first_use_date"] = pd.to_datetime(df["first_use_date"], errors="coerce")
    df["completed_date"] = pd.to_datetime(df["completed_date"], errors="coerce")

    df["test_mileage"] = pd.to_numeric(df["test_mileage"], errors="coerce")
    df["cylinder_capacity"] = pd.to_numeric(df["cylinder_capacity"], errors="coerce")

    df["vehicle_age"] = (
        df["test_date"] - df["first_use_date"]
    ).dt.days / 365.25

    df["vehicle_age_group"] = pd.cut(
        df["vehicle_age"],
        bins=[0, 3, 5, 8, 10, 15, float("inf")],
        labels=["0-3", "3-5", "5-8", "8-10", "10-15", "15+"]
    )

    df["mileage_group"] = pd.cut(
        df["test_mileage"],
        bins=[-1, 20000, 50000, 100000, 150000, 200000, float("inf")],
        labels=["0-20k", "20-50k", "50-100k", "100-150k", "150-200k", "200k+"]
    )

    df.to_csv(
        output_file,
        mode="w" if first_file else "a",
        header=first_file,
        index=False
    )

    first_file = False
    print("Completed:", os.path.basename(file))

print("FINAL 2024 CLEANING COMPLETED")
print("Saved:", output_file)