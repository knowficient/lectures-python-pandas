import pandas as pd
d_set1 = pd.read_csv("autodata-p1.csv")
d_set2 = pd.read_csv("autodata-p2.csv")
d_setc = pd.concat([d_set1,d_set2])
print(d_setc)
