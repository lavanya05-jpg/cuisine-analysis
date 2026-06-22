import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv(r"C:\Users\lavanya\Downloads\cuisine_analysis\dataset.csv", on_bad_lines='skip')

# ── Part 1: Keyword Analysis ──
positive_labels = ["Excellent", "Very Good", "Good"]
negative_labels = ["Average", "Poor"]

positive_reviews = df[df["Rating text"].isin(positive_labels)]["Rating text"]
negative_reviews = df[df["Rating text"].isin(negative_labels)]["Rating text"]

pos_counts = Counter(positive_reviews)
neg_counts = Counter(negative_reviews)

print("Top Positive Keywords:", pos_counts.most_common())
print("Top Negative Keywords:", neg_counts.most_common())

# Positive bar chart
plt.figure(figsize=(8, 4))
plt.bar(pos_counts.keys(), pos_counts.values(), color="green")
plt.title("Positive Review Keywords")
plt.savefig(r"C:\Users\lavanya\Downloads\cuisine_analysis\positive_keywords.png")
plt.show()

# Negative bar chart
plt.figure(figsize=(8, 4))
plt.bar(neg_counts.keys(), neg_counts.values(), color="red")
plt.title("Negative Review Keywords")
plt.savefig(r"C:\Users\lavanya\Downloads\cuisine_analysis\negative_keywords.png")
plt.show()

# ── Part 2: Review Length vs Rating ──
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df_clean = df.dropna(subset=["Votes", "Aggregate rating"])

avg_length = df_clean["Votes"].mean()
print(f"\nAverage Votes (Review Length Proxy): {avg_length:.2f}")

correlation = df_clean["Votes"].corr(df_clean["Aggregate rating"])
print(f"Correlation between Votes and Rating: {correlation:.4f}")

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df_clean["Votes"], df_clean["Aggregate rating"], alpha=0.3, color="steelblue")
plt.xlabel("Votes (Review Length Proxy)")
plt.ylabel("Aggregate Rating")
plt.title("Review Length vs Rating")
plt.savefig(r"C:\Users\lavanya\Downloads\cuisine_analysis\review_length_vs_rating.png")
plt.show()
