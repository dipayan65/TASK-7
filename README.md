# Task 7 - Sales Summary with SQLite and Python

## 📌 Objective
Use SQL inside Python to pull simple sales info like total quantity sold and total revenue, and display it using print statements and a bar chart.

## 🧰 Tools Used
- Python
- SQLite3 (built-in with Python)
- pandas
- matplotlib

## 📁 Files
- `task7_sales_summary.py` — Main Python script
- `sales_data.db` — SQLite database with sample sales data
- `sales_chart.png` — Generated bar chart of revenue by product (created on running script)

## 🚀 What It Does
1. Creates a `sales` table and inserts sample data (if not already present).
2. Runs an SQL query to calculate:
   - Total quantity sold per product
   - Total revenue per product
3. Displays the results using `pandas`.
4. Visualizes the revenue by product using `matplotlib`.

## 📊 Sample Output
The bar chart shows revenue per product with proper labeling.
