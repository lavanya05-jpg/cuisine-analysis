import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

cuisines = df["Cuisines"].dropna().str.split(", ").explode()
top_cuisines = cuisines.value_counts().head(3)

plt.figure(figsize=(6,4))
top_cuisines.plot(kind="bar")
plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()