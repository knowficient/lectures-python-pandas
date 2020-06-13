import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
d_set["Tax"] = d_set.eval("price*0.07")
print(d_set)