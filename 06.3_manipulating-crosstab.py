import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
ct = pd.crosstab(d_set.company, d_set.body_style)
print(ct)