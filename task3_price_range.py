import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset.csv")

# Step 1: Count how many restaurants fall into each price range
price_counts = df['Price range'].value_counts().sort_index()
print("Restaurant count per price range:")
print(price_counts)

# Step 2: Calculate percentage of restaurants in each price range
price_percentages = (price_counts / price_counts.sum()) * 100
print("\nPercentage of restaurants per price range:")
print(price_percentages.round(2))

# Step 3: Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(price_counts.index.astype(str), price_counts.values, color='#1de9b6', edgecolor='black')
plt.title('Distribution of Restaurants by Price Range', fontsize=14)
plt.xlabel('Price Range (1 = Low, 4 = High)', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add percentage labels on top of each bar
for i, (count, pct) in enumerate(zip(price_counts.values, price_percentages.values)):
    plt.text(i, count + 50, f"{pct:.1f}%", ha='center', fontsize=10)

plt.tight_layout()

# Step 4: Save the chart as an image AND show it
plt.savefig("price_range_distribution.png", dpi=200)
plt.show()