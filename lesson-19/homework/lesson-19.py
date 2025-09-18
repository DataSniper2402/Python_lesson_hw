import pandas as pd
# HOMEWORK-1

# 1
sales = pd.read_csv("task/sales_data.csv")

# 2
category_stats = sales.groupby("Category").agg(
    Total_Quantity=("Quantity", "sum"),
    Avg_Price=("Price", "mean"),
    Max_Quantity=("Quantity", "max")
).reset_index()

print("Category-wise statistics:")
print(category_stats)

# 3
top_products = (
    sales.groupby(["Category", "Product"])["Quantity"]
    .sum()
    .reset_index()
    .sort_values(["Category", "Quantity"], ascending=[True, False])
)

top_products = top_products.groupby("Category").head(1)
print("\nTop-selling product in each category:")
print(top_products)

# 4
sales["Total"] = sales["Quantity"] * sales["Price"]
best_date = (
    sales.groupby("Date")["Total"]
    .sum()
    .reset_index()
    .sort_values("Total", ascending=False)
    .head(1)
)
print("\nDate with highest sales:")
print(best_date)


# HOMEWORK-2

#1
orders = pd.read_csv("task/customer_orders.csv")

#2
customer_order_counts = orders.groupby("CustomerID")["OrderID"].nunique().reset_index()
valid_customers = customer_order_counts[customer_order_counts["OrderID"] >= 20]

print("Customers with at least 20 orders:")
print(valid_customers)

# 3
avg_price_per_customer = orders.groupby("CustomerID")["Price"].mean().reset_index()
high_price_customers = avg_price_per_customer[avg_price_per_customer["Price"] > 120]

print("\nCustomers with average price > $120:")
print(high_price_customers)

# 4
product_stats = orders.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("Price", "sum")
).reset_index()

filtered_products = product_stats[product_stats["Total_Quantity"] >= 5]
print("\nProducts with total quantity >= 5:")
print(filtered_products)

# HOMEWORK-3

import sqlite3
import numpy as np

# 1
conn = sqlite3.connect("task/population.db")
population = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# 2
salary_bands = pd.read_excel("task/population salary analysis.xlsx")


def categorize_salary(salary, bands):
    for _, row in bands.iterrows():
        if row["Min"] <= salary <= row["Max"]:
            return row["Band"]
    return "Other"

population["Salary_Band"] = population["Salary"].apply(lambda x: categorize_salary(x, salary_bands))

# 3
overall_stats = population.groupby("Salary_Band").agg(
    Population_Count=("Salary", "count"),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
).reset_index()

overall_stats["Percentage"] = (overall_stats["Population_Count"] / len(population)) * 100
print("Overall Salary Band Statistics:")
print(overall_stats)

# 4
state_stats = population.groupby(["State", "Salary_Band"]).agg(
    Population_Count=("Salary", "count"),
    Avg_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
).reset_index()

state_stats["Percentage"] = (
    state_stats.groupby("State")["Population_Count"].transform(lambda x: (x / x.sum()) * 100)
)

print("\nPer-State Salary Band Statistics:")
print(state_stats)

