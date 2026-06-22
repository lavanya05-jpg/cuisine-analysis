import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\lavanya\Downloads\cuisine_analysis\dataset.csv")

# Clean votes column
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df_clean = df.dropna(subset=["Votes", "Aggregate rating"])

# ── Part 1: Highest and Lowest Votes ──
highest = df_clean.loc[df_clean["Votes"].idxmax()]
lowest = df_clean.loc[df_clean["Votes"].idxmin()]

print("Restaurant with HIGHEST votes:")
print(f"  Name: {highest['Restaurant Name']}")
print(f"  Votes: {highest['Votes']}")
print(f"  Rating: {highest['Aggregate rating']}")

print("\nRestaurant with LOWEST votes:")
print(f"  Name: {lowest['Restaurant Name']}")
print(f"  Votes: {lowest['Votes']}")
print(f"  Rating: {lowest['Aggregate rating']}")

# ── Part 2: Correlation ──
correlation = df_clean["Votes"].corr(df_clean["Aggregate rating"])
print(f"\nCorrelation between Votes and Rating: {correlation:.4f}")

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df_clean["Votes"], df_clean["Aggregate rating"], alpha=0.3, color="steelblue")
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate Rating")
plt.title("Votes vs Rating Correlation")
plt.savefig(r"C:\Users\lavanya\Downloads\cuisine_analysis\votes_vs_rating.png")
plt.show()

print("\nChart saved as votes_vs_rating.png")