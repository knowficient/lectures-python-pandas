import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
d_set.rename(columns={'company':'brand'},inplace=True)
print(d_set)