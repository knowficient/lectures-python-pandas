import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
c_set = d_set.drop("horsepower",axis=1)
print(c_set)