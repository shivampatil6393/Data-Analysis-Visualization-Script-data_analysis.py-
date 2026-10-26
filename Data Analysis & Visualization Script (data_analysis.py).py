import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- OBJECTIVE 1 & 2: Load and Explore Dataset ---
# Creating a sample monthly sales dataset with some missing (NaN) values
data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
    "Sales": [
        2500,
        2700,
        np.nan,
        3100,
        3500,
        4200,
        4000,
        3800,
        np.nan,
        4600,
        4900,
        5300,
    ],
    "Expenses": [
        1800,
        1900,
        2000,
        2100,
        2300,
        2500,
        2400,
        2600,
        2700,
        2800,
        3000,
        3200,
    ],
    "Region": [
        "North",
        "South",
        "North",
        "East",
        "West",
        "East",
        "South",
        "North",
        "West",
        "East",
        "South",
        "North",
    ],
}

df = pd.DataFrame(data)

print("--- 1. Initial Dataset Overview ---")
print(df.head(10))
print("\nDataset Information:")
print(df.info())


# --- OBJECTIVE 3: Data Cleaning & Analysis ---
# Fill missing Sales values with the average (mean) sales
mean_sales = df["Sales"].mean()
df["Sales"] = df["Sales"].fillna(mean_sales)
print(f"\n--- Cleaned Data (Missing Sales filled with {mean_sales:.2f}) ---")

# Calculate Profit
df["Profit"] = df["Sales"] - df["Expenses"]

print("\n--- Summary Statistics ---")
print(df.describe())

# Group analysis: Total sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\n--- Total Sales by Region ---")
print(region_sales)


# --- OBJECTIVE 4: Data Visualization using Matplotlib ---
plt.figure(figsize=(15, 5))

# 1. Line Chart: Sales vs Expenses over time
plt.subplot(1, 3, 1)
plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    color="dodgerblue",
    label="Sales",
    linewidth=2,
)
plt.plot(
    df["Month"],
    df["Expenses"],
    marker="s",
    color="crimson",
    label="Expenses",
    linewidth=2,
)
plt.title("Monthly Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# 2. Bar Chart: Total Sales by Region
plt.subplot(1, 3, 2)
region_sales.plot(kind="bar", color=["#4CAF50", "#FF9800", "#03A9F4", "#E91E63"])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)

# 3. Pie Chart: Sales Share by Region
plt.subplot(1, 3, 3)
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
plt.title("Sales Share by Region")
plt.ylabel("")  # Remove default y-label

plt.tight_layout()
plt.show()