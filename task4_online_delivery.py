import pandas as pd

df = pd.read_csv(r"C:\Users\lavanya\Downloads\cuisine_analysis\dataset.csv", on_bad_lines='skip')
print(df.columns.tolist())