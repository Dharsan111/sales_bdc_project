import pandas as pd
import os

print("CLEANING STARTED 🚀")

base_path = os.path.dirname(os.path.dirname(__file__))

input_path = os.path.join(base_path, 'data', 'raw', 'sales_data.csv')
output_path = os.path.join(base_path, 'data', 'cleaned', 'cleaned_sales_data.csv')

df = pd.read_csv(input_path)

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df['quantity'] = df['quantity'].fillna(1)
df['customer'] = df['customer'].fillna("Unknown")
df['product'] = df['product'].fillna("Unknown")
df['region'] = df['region'].fillna("Unknown")

# Fix date issues
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])  # remove invalid dates

# Remove negative quantity
df = df[df['quantity'] > 0]

# Save cleaned data
df.to_csv(output_path, index=False)

print("Cleaned Data:")
print(df)

print("✅ CLEANING DONE")