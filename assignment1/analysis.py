import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, "data.csv"))

# Check the data
print(df.head())
print(df.info())

# Get average sales
avg = df["Sales"].mean()
print(f"average Sales: {avg}")

# Bar chart for sales by category
sales_by_cat = df.groupby("Category")["Sales"].mean()
plt.figure(figsize=(8, 5))
plt.bar(sales_by_cat.index, sales_by_cat.values)
plt.title("Average Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Compare sales and profit
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# Check correlations
corr = df.select_dtypes(include=['number']).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
