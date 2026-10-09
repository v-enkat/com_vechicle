# 2. Mileage vs Failure Rate

import pandas as pd
import matplotlib.pyplot as plt

file_path = r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\datasets\cleaned_2024_final.csv"

mileage_bins = [-1, 20000, 50000, 100000, 150000, 200000, float("inf")]
mileage_labels = ["0-20k", "20-50k", "50-100k", "100-150k", "150-200k", "200k+"]

stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["test_mileage", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk["test_mileage"] = pd.to_numeric(chunk["test_mileage"], errors="coerce")
    chunk = chunk.dropna(subset=["test_mileage"])

    chunk["mileage_group"] = pd.cut(
        chunk["test_mileage"],
        bins=mileage_bins,
        labels=mileage_labels
    )

    temp = chunk.groupby("mileage_group", observed=False)["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    stats.append(temp)

mileage = pd.concat(stats).groupby(level=0).sum()
mileage["failure_rate"] = mileage["failures"] / mileage["total"] * 100

print("\n2024 MILEAGE VS FAILURE RATE")
print(mileage)

plt.figure(figsize=(9, 5))
plt.plot(mileage.index.astype(str), mileage["failure_rate"], marker="o")
plt.title("2024 Failure Rate by Mileage")
plt.xlabel("Mileage Group")
plt.ylabel("Failure Rate (%)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\trend_analysis.png"
)
# 3. Vehicle Age vs Failure Rate

import pandas as pd
import matplotlib.pyplot as plt

age_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["vehicle_age", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk["vehicle_age"] = pd.to_numeric(chunk["vehicle_age"], errors="coerce")
    chunk = chunk.dropna(subset=["vehicle_age"])

    chunk["age_group"] = pd.cut(
        chunk["vehicle_age"],
        bins=[0, 3, 5, 8, 10, 15, float("inf")],
        labels=["0-3", "3-5", "5-8", "8-10", "10-15", "15+"]
    )

    temp = chunk.groupby("age_group", observed=False)["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    age_stats.append(temp)

age = pd.concat(age_stats).groupby(level=0).sum()
age["failure_rate"] = age["failures"] / age["total"] * 100

print("\n2024 VEHICLE AGE VS FAILURE RATE")
print(age)

plt.figure(figsize=(9, 5))
plt.plot(age.index.astype(str), age["failure_rate"], marker="o")
plt.title("2024 Failure Rate by Vehicle Age")
plt.xlabel("Vehicle Age Group")
plt.ylabel("Failure Rate (%)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\age_failure_rate.png"
)
# 4. Make-wise Failure Rate

make_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["make", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["make"])

    temp = chunk.groupby("make")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    make_stats.append(temp)

make = pd.concat(make_stats).groupby(level=0).sum()

make["failure_rate"] = make["failures"] / make["total"] * 100

make = make[make["total"] >= 100]
make = make.sort_values("failure_rate", ascending=False)

print("\n2024 TOP 10 MAKES BY FAILURE RATE")
print(make.head(10))

plt.figure(figsize=(10, 6))
make.head(10)["failure_rate"].sort_values().plot(kind="barh")
plt.title("2024 Top 10 Vehicle Makes by Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Vehicle Make")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\make_failure_rate.png"
)
# 5. Fuel Type vs Failure Rate

fuel_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["fuel_type", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["fuel_type"])

    temp = chunk.groupby("fuel_type")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    fuel_stats.append(temp)

fuel = pd.concat(fuel_stats).groupby(level=0).sum()

fuel["failure_rate"] = fuel["failures"] / fuel["total"] * 100

fuel = fuel[fuel["total"] >= 100]
fuel = fuel.sort_values("failure_rate", ascending=False)

print("\n2024 FUEL TYPE VS FAILURE RATE")
print(fuel)

plt.figure(figsize=(10, 6))
fuel["failure_rate"].sort_values().plot(kind="barh")

plt.title("2024 Fuel Type vs Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Fuel Type")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\fuel_failure_rate.png"
)
# 6. Test Class-wise Failure Rate

class_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["test_class_id", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["test_class_id"])

    temp = chunk.groupby("test_class_id")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    class_stats.append(temp)

test_class = pd.concat(class_stats).groupby(level=0).sum()

test_class["failure_rate"] = (
    test_class["failures"] / test_class["total"] * 100
)

test_class = test_class[test_class["total"] >= 100]
test_class = test_class.sort_values("failure_rate", ascending=False)

print("\n2024 TEST CLASS VS FAILURE RATE")
print(test_class)

plt.figure(figsize=(10, 6))
test_class["failure_rate"].sort_values().plot(kind="barh")

plt.title("2024 Test Class vs Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Test Class")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\test_class_failure_rate.png"
)
# 7. Model-wise Failure Rate

model_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["model", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["model"])

    temp = chunk.groupby("model")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    model_stats.append(temp)

model = pd.concat(model_stats).groupby(level=0).sum()

model["failure_rate"] = (
    model["failures"] / model["total"] * 100
)

model = model[model["total"] >= 500]
model = model.sort_values("failure_rate", ascending=False)

print("\n2024 TOP 10 MODELS BY FAILURE RATE")
print(model.head(10))

plt.figure(figsize=(10, 6))
model.head(10)["failure_rate"].sort_values().plot(kind="barh")

plt.title("2024 Top 10 Vehicle Models by Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Vehicle Model")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\model_failure_rate.png"
)
# 8. Postcode Area vs Failure Rate

postcode_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["postcode_area", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["postcode_area"])

    temp = chunk.groupby("postcode_area")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    postcode_stats.append(temp)

postcode = pd.concat(postcode_stats).groupby(level=0).sum()

postcode["failure_rate"] = (
    postcode["failures"] / postcode["total"] * 100
)

postcode = postcode[postcode["total"] >= 500]
postcode = postcode.sort_values("failure_rate", ascending=False)

print("\n2024 TOP 10 POSTCODE AREAS BY FAILURE RATE")
print(postcode.head(10))

plt.figure(figsize=(10, 6))
postcode.head(10)["failure_rate"].sort_values().plot(kind="barh")

plt.title("2024 Top 10 Postcode Areas by Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Postcode Area")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\postcode_failure_rate.png"
)
# 9. Month-wise Failure Rate

month_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["test_date", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk["test_date"] = pd.to_datetime(chunk["test_date"], errors="coerce")
    chunk = chunk.dropna(subset=["test_date"])

    chunk["month"] = chunk["test_date"].dt.month

    temp = chunk.groupby("month")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    month_stats.append(temp)

monthly = pd.concat(month_stats).groupby(level=0).sum()

monthly["failure_rate"] = (
    monthly["failures"] / monthly["total"] * 100
)

print("\n2024 MONTH-WISE FAILURE RATE")
print(monthly)

plt.figure(figsize=(10, 6))
plt.plot(
    monthly.index,
    monthly["failure_rate"],
    marker="o"
)

plt.title("2024 Monthly Failure Rate Trend")
plt.xlabel("Month")
plt.ylabel("Failure Rate (%)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\monthly_failure_trend.png"
)
# 10. Vehicle Colour vs Failure Rate

colour_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["colour", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["colour"])

    temp = chunk.groupby("colour")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    colour_stats.append(temp)

colour = pd.concat(colour_stats).groupby(level=0).sum()

colour["failure_rate"] = (
    colour["failures"] / colour["total"] * 100
)

colour = colour[colour["total"] >= 500]
colour = colour.sort_values("failure_rate", ascending=False)

print("\n2024 TOP 10 VEHICLE COLOURS BY FAILURE RATE")
print(colour.head(10))

plt.figure(figsize=(10, 6))
colour.head(10)["failure_rate"].sort_values().plot(kind="barh")

plt.title("2024 Top 10 Vehicle Colours by Failure Rate")
plt.xlabel("Failure Rate (%)")
plt.ylabel("Vehicle Colour")
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\colour_failure_rate.png"
)
# 11. Cylinder Capacity vs Failure Rate

capacity_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["cylinder_capacity", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["cylinder_capacity"])

    chunk["capacity_group"] = pd.cut(
        chunk["cylinder_capacity"],
        bins=[0, 1000, 1500, 2000, 2500, 3000, 4000, float("inf")],
        labels=[
            "0-1000",
            "1000-1500",
            "1500-2000",
            "2000-2500",
            "2500-3000",
            "3000-4000",
            "4000+"
        ]
    )

    temp = chunk.groupby("capacity_group", observed=False)["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    capacity_stats.append(temp)

capacity = pd.concat(capacity_stats).groupby(level=0).sum()

capacity["failure_rate"] = (
    capacity["failures"] / capacity["total"] * 100
)

print("\n2024 CYLINDER CAPACITY VS FAILURE RATE")
print(capacity)

plt.figure(figsize=(10, 6))
capacity["failure_rate"].plot(kind="bar")

plt.title("2024 Cylinder Capacity vs Failure Rate")
plt.xlabel("Cylinder Capacity (cc)")
plt.ylabel("Failure Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\cylinder_capacity_failure_rate.png"
)
# 12. Test Type vs Failure Rate

test_type_stats = []

for chunk in pd.read_csv(
    file_path,
    usecols=["test_type", "test_result"],
    escapechar="\\",
    chunksize=500000,
    low_memory=False
):
    chunk = chunk.dropna(subset=["test_type"])

    temp = chunk.groupby("test_type")["test_result"].agg(
        total="count",
        failures=lambda x: (x == "F").sum()
    )

    test_type_stats.append(temp)

test_type = pd.concat(test_type_stats).groupby(level=0).sum()

test_type["failure_rate"] = (
    test_type["failures"] / test_type["total"] * 100
)

print("\n2024 TEST TYPE VS FAILURE RATE")
print(test_type)

plt.figure(figsize=(10, 6))
test_type["failure_rate"].plot(kind="bar")

plt.title("2024 Test Type vs Failure Rate")
plt.xlabel("Test Type")
plt.ylabel("Failure Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\Visualizations\test_type_failure_rate.png"
)