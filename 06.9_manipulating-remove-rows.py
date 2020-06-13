import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
r_set = d_set.drop(d_set.index[2:4])
print(r_set)