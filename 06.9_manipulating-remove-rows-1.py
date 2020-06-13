import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
r_set = d_set.drop(1,axis=0)
print(r_set)