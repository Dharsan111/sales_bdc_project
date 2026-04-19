import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

print("ANALYSIS FROM MYSQL 🚀")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="test123",
    database="sales_project"
)

# Fetch full table (no complex query)
df = pd.read_sql("SELECT * FROM sales", conn)

print("✅ Data fetched")

# Create output path
base_path = os.path.dirname(os.path.dirname(__file__))
output_path = os.path.join(base_path, 'outputs', 'charts', 'revenue_profit.png')

# Group by product
grouped = df.groupby('product')[['revenue', 'profit']].sum()

print(grouped)

# Plot bar chart
grouped.plot(kind='bar')
plt.title("Revenue vs Profit by Product")
plt.ylabel("Amount")

# Save chart
plt.savefig(output_path)
plt.show()

print("✅ Chart saved at:", output_path)

conn.close()