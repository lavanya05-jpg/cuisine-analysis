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
