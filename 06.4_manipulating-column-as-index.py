import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
d_set.set_index("company", inplace=True)
print(d_set)