import pandas as pd

d_set = pd.read_csv("autodata.csv")

print("\nReturns the unique categories")
print(d_set["body_style"].unique())

print("\nReturns the number of rows of unique categories")
print(d_set["body_style"].nunique())