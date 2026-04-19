import pandas as pd
import os

print("TRANSFORMATION STARTED 🚀")

base_path = os.path.dirname(os.path.dirname(__file__))

input_path = os.path.join(base_path, 'data', 'cleaned', 'cleaned_sales_data.csv')
output_path = os.path.join(base_path, 'data', 'cleaned', 'fact_sales.csv')

df = pd.read_csv(input_path)

# Add new business facts
df['revenue'] = df['quantity'] * df['price']
df['discount'] = df['revenue'] * 0.1   # 10% discount
df['net_revenue'] = df['revenue'] - df['discount']
df['cost'] = df['revenue'] * 0.6       # assume cost is 60%
df['profit'] = df['net_revenue'] - df['cost']

# Final fact table
fact_sales = df[[
    'order_id',
    'date',
    'customer',
    'product',
    'region',
    'quantity',
    'price',
    'revenue',
    'discount',
    'net_revenue',
    'cost',
    'profit'
]]

fact_sales.to_csv(output_path, index=False)

print("✅ TRANSFORMATION DONE")
print(fact_sales.head())