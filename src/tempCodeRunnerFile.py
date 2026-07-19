import pandas as pd

df = pd.read_csv(r"C:\Users\Saksham sharma\Desktop\Traffic prediction\data\raw\Metro-Interstate-Traffic-Volume-Encoded.csv")

print(df.head())

df .isnull().sum()
