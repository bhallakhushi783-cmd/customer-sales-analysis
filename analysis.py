import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("customer_sales.csv")

# Create Total Sales
df["Total_Sales"] = df["Price"] * df["Quantity"]

# Create Category
df["Category"] = df["Total_Sales"].apply(
    lambda x: "High" if x > 50000 
    else "Medium" if x > 20000 
    else "Low"
)

# City-wise sales
city_sales = df.groupby("City")["Total_Sales"].sum().reset_index()

# Product-wise sales
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

# Top 3 products
top_products = product_sales.sort_values(by="Total_Sales", ascending=False).head(3)

# Top 3 customers
top_customers = df.groupby("Customer")["Total_Sales"].sum().reset_index()
top_customers = top_customers.sort_values(by="Total_Sales", ascending=False).head(3)

# Category distribution
category_counts = df["Category"].value_counts()

# -------- DASHBOARD --------

plt.figure(figsize=(14,8))

# 1. City-wise Sales
plt.subplot(2,3,1)
plt.bar(city_sales["City"], city_sales["Total_Sales"])
plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)

# 2. Product-wise Sales (ALL products)
plt.subplot(2,3,2)
plt.bar(product_sales["Product"], product_sales["Total_Sales"])
plt.title("All Products Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# 3. Top 3 Products
plt.subplot(2,3,3)
plt.bar(top_products["Product"], top_products["Total_Sales"])
plt.title("Top 3 Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# 4. Top 3 Customers
plt.subplot(2,3,4)
plt.bar(top_customers["Customer"], top_customers["Total_Sales"])
plt.title("Top Customers")
plt.xlabel("Customers")
plt.ylabel("Total Sales")

# 5. Category Distribution
plt.subplot(2,3,5)
plt.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%")
plt.title("Customer Categories Distribution")

plt.tight_layout()
plt.show()

# -------- INSIGHTS --------

print("Top City:", city_sales.sort_values(by="Total_Sales", ascending=False).iloc[0]["City"])
print("Top Product:", product_sales.sort_values(by="Total_Sales", ascending=False).iloc[0]["Product"])
print("Top Customer:", top_customers.iloc[0]["Customer"])