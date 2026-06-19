# Top Cuisines Analysis

## Objective

Analyze restaurant data to identify the top three most common cuisines and calculate the percentage of restaurants serving them.

## Tools Used

* Python
* Pandas
* Matplotlib

## Dataset

Restaurant dataset provided as part of the Cognifyz Data Analysis Internship.

## Results

| Cuisine      | Count | Percentage |
| ------------ | ----- | ---------- |
| North Indian | 3960  | 41.46%     |
| Chinese      | 2735  | 28.64%     |
| Fast Food    | 1986  | 20.79%     |

## Bar Chart Visualization
<img width="600" height="400" alt="Figure_1" src="https://github.com/user-attachments/assets/be014cb8-2ad6-4ae2-9c65-db70460fbfe1" />


The following bar chart was created to visualize the distribution of the top three cuisines:

```python
import pandas as pd
import matplotlib.pyplot as plt

cuisines = ['North Indian', 'Chinese', 'Fast Food']
counts = [3960, 2735, 1986]

plt.figure(figsize=(8, 5))
plt.bar(cuisines, counts, color=['#4CAF50', '#2196F3', '#FF9800'])
plt.title('Top 3 Most Common Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Number of Restaurants')
plt.show()
```

### Sample Output

```
North Indian | ████████████████████████████████████████ 3960
Chinese      | ███████████████████████████ 2735
Fast Food    | ████████████████████ 1986
```

## Conclusion

North Indian cuisine is the most popular cuisine in the dataset, accounting for 41.46% of restaurants. Chinese cuisine ranks second with 28.64%, followed by Fast Food at 20.79%. The bar chart clearly highlights the popularity difference among the top three cuisines.

## Author

Lavanya Arya
## Task 2: City Analysis

### Objective
- Identify the city with the highest number of restaurants in the dataset.
- Calculate the average rating for restaurants in each city.
- Determine the city with the highest average rating.

### Approach
1. Loaded the dataset using pandas (`dataset.csv`).
2. Used `value_counts()` on the `City` column to count restaurants per city.
3. Used `groupby('City')` on the `Aggregate rating` column to calculate average rating per city.
4. Cross-checked the top average ratings against restaurant count per city, since cities with very few restaurants can show misleadingly high averages.

### Results

**City with the most restaurants:** New Delhi, with 5473 restaurants (by far the largest in the dataset, ahead of Gurgaon at 1118).

**Average rating by city (top 5):**

| City              | Average Rating | Restaurant Count |
|-------------------|-----------------|-------------------|
| Inner City        | 4.90            | 2                 |
| Quezon City       | 4.80            | 1                 |
| Makati City       | 4.65            | 2                 |
| Pasig City        | 4.63            | 3                 |
| Mandaluyong City  | 4.625           | 4                 |

**City with the highest average rating:** Inner City (4.90), but this is based on only 2 restaurants, so it isn't statistically meaningful. Most top-rated cities in this dataset have very few restaurants. The most reliable high-rated city with a meaningful sample size is **London**, with an average rating of 4.535 across 20 restaurants.

### Files
- `task2_city_analysis.py` — analysis script
- `dataset.csv` — dataset used
## Task 3: Price Range Distribution

### Objective
- Create a bar chart to visualize the distribution of price ranges among restaurants.
- Calculate the percentage of restaurants in each price range category.

### Approach
1. Loaded the dataset using pandas (`dataset.csv`).
2. Used `value_counts()` on the `Price range` column to count restaurants per category.
3. Calculated each category's percentage of the total restaurant count.
4. Created a bar chart using matplotlib, with percentage labels on top of each bar.

### Results
<img width="800" height="503" alt="task3 (1)" src="https://github.com/user-attachments/assets/f71589b2-ac82-469e-b853-53c21fe60900" />

### Files
- `task3_price_range.py` — analysis and chart script
- `price_range_distribution.png` — output chart image
<<<<<<< HEAD
## Task 4: Online Delivery

### Objective
- Determine the percentage of restaurants that offer online delivery.
- Compare the average ratings of restaurants with and without online delivery.

### Approach
1. Loaded the dataset using pandas (`dataset.csv`).
2. Used `value_counts()` on the `Has Online delivery` column to count restaurants in each category.
3. Calculated the percentage of restaurants offering online delivery.
4. Used `groupby('Has Online delivery')` on the `Aggregate rating` column to compare average ratings between the two groups.

### Results

**Percentage of restaurants offering online delivery:**
- No online delivery: 74.34%
- Has online delivery: 25.66%

**Average rating comparison:**
| Online Delivery | Average Rating |
|------------------|------------------|
| No               | 2.47             |
| Yes              | 3.25             |

Restaurants that offer online delivery have a noticeably higher average rating (3.25) compared to those that don't (2.47), a difference of nearly 0.8 points. Since both groups contain thousands of restaurants, this isn't a small-sample fluke like some results in Task 2, it's a meaningful pattern. This could be because delivery-enabled restaurants tend to be more established, more customer-focused, or operate in markets where customer experience standards (and review culture) are higher.

### Files
- `task4_online_delivery.py` — analysis script
=======
>>>>>>> d4b0bd7e74839f51ab82ff952318ff524168b3fb
