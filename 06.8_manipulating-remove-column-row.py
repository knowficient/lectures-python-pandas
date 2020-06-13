import pandas as pd

d_set = pd.read_csv("autodata-2.csv")

c_set = d_set.drop("horsepower",axis=1) #drop column horsepower
print(c_set)

r_set = d_set.drop(1, axis=0)           #drop row number 1
print(r_set)