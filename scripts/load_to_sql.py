import pandas as pd
import mysql.connector
import os

print("LOADING DATA TO MYSQL 🚀")

# Base path
base_path = os.path.dirname(os.path.dirname(__file__))

# File path
file_path = os.path.join(base_path, 'data', 'cleaned', 'fact_sales.csv')

# Load CSV
df = pd.read_csv(file_path)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="test123",
    database="sales_project"
)

cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (
            order_id, date, customer, product, region,
            quantity, price, revenue, discount,
            net_revenue, cost, profit
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

print("✅ Data inserted into MySQL")

cursor.close()
conn.close()