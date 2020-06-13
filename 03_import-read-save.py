import pandas as pd

d_set = pd.read_csv("autodata.csv")
d_set.to_csv("new-audodata.csv", index=False)