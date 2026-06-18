import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.shape)        # confirms rows/columns loaded correctly
print(df.columns)      # sanity check column names

# Step 1: City with the most restaurants
city_counts = df['City'].value_counts()
print("\nTop 10 cities by number of restaurants:")
print(city_counts.head(10))

top_city = city_counts.idxmax()
top_city_count = city_counts.max()
print(f"\nCity with most restaurants: {top_city} ({top_city_count} restaurants)")

# Step 2: Average rating per city
avg_rating_by_city = df.groupby('City')['Aggregate rating'].mean()
print("\nTop 10 cities by average rating:")
print(avg_rating_by_city.sort_values(ascending=False).head(10))

# Step 3: City with the highest average rating
top_rated_city = avg_rating_by_city.idxmax()
top_rated_value = avg_rating_by_city.max()
print(f"\nCity with highest average rating: {top_rated_city} ({top_rated_value:.2f})")
# Step 4: Check rating alongside restaurant count to avoid misleading averages
city_rating_count = df.groupby('City')['Aggregate rating'].agg(['mean', 'count'])
city_rating_count_sorted = city_rating_count.sort_values('mean', ascending=False)
print("\nTop 10 cities by average rating, with restaurant count:")
print(city_rating_count_sorted.head(10))