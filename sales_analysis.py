import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data
df = pd.read_csv("sales_data.csv")

# Display data
print("Dataset Preview:")
print(df.head())

# Create Total Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Total sales per month
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
print("\nTotal Sales Per Month:")
print(monthly_sales)

# Best-selling product
best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("\nBest-Selling Product:", best_selling_product)

# Plot Monthly Sales Trend
plt.figure()
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Plot Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

plt.figure()
sns.barplot(x="Product", y="Total_Sales", data=product_sales)
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.show()

print("\nSales analysis completed successfully!")
