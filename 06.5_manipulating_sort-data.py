import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
sv = d_set.sort_values("price", ascending=True)
print(sv)