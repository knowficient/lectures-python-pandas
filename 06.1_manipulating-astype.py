import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
d_set.price = d_set.price.astype(float)
print(d_set[["price"]])