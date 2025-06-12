
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create and populate the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sample_data = [
    ("Apple", 10, 1.5),
    ("Banana", 20, 0.5),
    ("Apple", 5, 1.5),
    ("Orange", 8, 1.2),
    ("Banana", 10, 0.5),
    ("Orange", 12, 1.2)
]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 2: Run query and analyze
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Step 3: Print results
print("Sales Summary:")
print(df)

# Step 4: Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
