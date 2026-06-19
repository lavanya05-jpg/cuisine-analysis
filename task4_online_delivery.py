import pandas as pd

# Load the dataset
df = pd.read_csv("dataset.csv")

# Step 1: Percentage of restaurants offering online delivery
delivery_counts = df['Has Online delivery'].value_counts()
print("Restaurant count by online delivery status:")
print(delivery_counts)

delivery_percentages = (delivery_counts / delivery_counts.sum()) * 100
print("\nPercentage of restaurants by online delivery status:")
print(delivery_percentages.round(2))

# Step 2: Compare average ratings between restaurants with vs without online delivery
avg_rating_by_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()
print("\nAverage rating by online delivery status:")
print(avg_rating_by_delivery.round(2))