import pandas as pd

d_set = pd.read_csv("autodata.csv")

print("\nReturns the first n rows")
print(d_set.head(3))

print("\nReturns the last n rows")
print(d_set.tail(3))