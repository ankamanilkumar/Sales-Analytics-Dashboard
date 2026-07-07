import pandas as pd

# Load the Excel file
df = pd.read_excel("../Dataset/Sales_Analytics_Dataset_100_Records.xlsx")

# Display the first 5 rows
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert the Order Date column to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create additional columns
df["Month"] = df["Order Date"].dt.month_name()
df["Year"] = df["Order Date"].dt.year
df["Quarter"] = df["Order Date"].dt.quarter
df["Day"] = df["Order Date"].dt.day_name()

# Save the cleaned data
df.to_csv("../Dataset/clean_sales.csv", index=False)

print("\nData cleaning completed successfully!")