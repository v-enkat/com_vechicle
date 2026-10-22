import pandas as pd

# Define the path of the raw January 2024 MOT dataset
file_path = r"D:\EDA PROJECT\Commercial Vehicle Reliability & Failure Pattern Analysis\datasets\raw_dataset.csv\test_result_202401.csv"

# Load the raw MOT test data
df = pd.read_csv(
    file_path,
    escapechar="\\"
)