import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
fd = d_set.company.value_counts(ascending=True)
print(fd)
