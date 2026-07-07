import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../Dataset/clean_sales.csv")

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_sales = df["Sales"].mean()
profit_margin = (total_profit / total_sales) * 100

print("=" * 50)
print("SALES ANALYTICS REPORT")
print("=" * 50)
print(f"Total Sales      : {total_sales}")
print(f"Total Profit     : {total_profit}")
print(f"Total Orders     : {total_orders}")
print(f"Average Sales    : {average_sales:.2f}")
print(f"Profit Margin    : {profit_margin:.2f}%")
print("=" * 50)

# Category Analysis
category_sales = df.groupby("Category")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

print("\nCategory Sales")
print(category_sales)

print("\nCategory Profit")
print(category_profit)

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# Top Customers
top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop Customers")
print(top_customers)

# Charts
monthly_sales.plot(kind="bar", figsize=(10,5))
plt.title("Monthly Sales")
plt.tight_layout()
plt.show()

category_sales.plot(kind="bar", figsize=(8,5))
plt.title("Sales by Category")
plt.tight_layout()
plt.show()

top_customers.plot(kind="bar", figsize=(10,5))
plt.title("Top 10 Customers")
plt.tight_layout()
plt.show()