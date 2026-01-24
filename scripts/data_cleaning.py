import pandas as pd

# File paths
RAW_FILE = "raw_data/customers_raw.csv"
CLEAN_FILE = "cleaned_data/customers_cleaned.csv"

print("Reading raw customer data...")
df = pd.read_csv(RAW_FILE)

print("Raw data:")
print(df)

# Remove rows with missing values
print("Cleaning data (dropping rows with nulls)...")
clean_df = df.dropna()

print("Cleaned data:")
print(clean_df)

# Save cleaned data
clean_df.to_csv(CLEAN_FILE, index=False)

print("Customer data cleaning completed successfully")
