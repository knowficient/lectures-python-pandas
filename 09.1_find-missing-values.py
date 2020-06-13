import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
print(d_set.isnull())