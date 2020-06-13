import pandas as pd

d_set = pd.read_csv("autodata.csv")

print("\nReturns the shape")
print(d_set.shape)

print("\nReturns the number of rows")
print(d_set.shape[0])

print("\nReturns the number of columns")
print(d_set.shape[1])