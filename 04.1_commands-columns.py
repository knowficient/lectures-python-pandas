import pandas as pd

d_set = pd.read_csv("autodata.csv")

print("\nReturns all columns")
print(d_set.columns)

print("\nSlicing the columns")
print(d_set.columns[0:2])