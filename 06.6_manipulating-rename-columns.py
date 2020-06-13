import pandas as pd

d_set = pd.read_csv("autodata-2.csv")
d_set.columns=["Index", "Company", "Body_Style", "Horsepower", "Average_Mileage", "Price"]
print(d_set)