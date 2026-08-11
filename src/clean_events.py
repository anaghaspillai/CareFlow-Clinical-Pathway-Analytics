import pandas as pd
import os

# ---- Step 1: Load the raw event log ----
input_path = "data/hospital_event_log.csv"
output_path = "data/hospital_event_log_clean.csv"

print("Loading raw event log...")
df = pd.read_csv(input_path)

original_row_count = len(df)
print(f"Loaded {original_row_count} rows.")

# ---- Step 2: Check for missing values ----
print("\nChecking for missing values...")
missing_summary = df.isnull().sum()
print(missing_summary)

# Drop rows with any missing Case_ID, Activity_Name, or Timestamp
df = df.dropna(subset=["Case_ID", "Activity_Name", "Timestamp"])
rows_after_dropna = len(df)
print(f"Rows dropped due to missing values: {original_row_count - rows_after_dropna}")

# ---- Step 3: Standardize Activity_Name formatting ----
print("\nStandardizing activity names...")
df["Activity_Name"] = df["Activity_Name"].str.strip()  # remove extra spaces
df["Activity_Name"] = df["Activity_Name"].str.title()  # consistent capitalization (e.g. "x-ray" -> "X-Ray")

# ---- Step 4: Convert Timestamp to proper datetime format ----
print("Converting timestamps to datetime format...")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# Drop rows where timestamp conversion failed (invalid dates)
rows_before_ts_check = len(df)
df = df.dropna(subset=["Timestamp"])
rows_after_ts_check = len(df)
print(f"Rows dropped due to invalid timestamps: {rows_before_ts_check - rows_after_ts_check}")

# ---- Step 5: Remove exact duplicate rows ----
print("\nChecking for duplicate rows...")
rows_before_dedup = len(df)
df = df.drop_duplicates()
rows_after_dedup = len(df)
print(f"Duplicate rows removed: {rows_before_dedup - rows_after_dedup}")

# ---- Step 6: Sort chronologically per patient (required for process mining) ----
print("\nSorting events by Case_ID and Timestamp...")
df = df.sort_values(by=["Case_ID", "Timestamp"]).reset_index(drop=True)

# ---- Step 7: Save cleaned data ----
os.makedirs("data", exist_ok=True)
df.to_csv(output_path, index=False)

# ---- Step 8: Final summary ----
print("\n===== CLEANING SUMMARY =====")
print(f"Original rows: {original_row_count}")
print(f"Final cleaned rows: {len(df)}")
print(f"Total rows removed: {original_row_count - len(df)}")
print(f"Unique patients (Case_ID): {df['Case_ID'].nunique()}")
print(f"Unique activities: {df['Activity_Name'].unique().tolist()}")
print(f"Cleaned file saved to: {output_path}")