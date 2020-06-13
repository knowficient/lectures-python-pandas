import pandas as pd

d_set = pd.read_csv("autodata.csv")

print("\nReturns all the datatypes")
print(d_set.dtypes)

print("\nReturns specific datatypes")
print(d_set.dtypes["price"])