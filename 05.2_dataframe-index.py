import pandas as pd
df = pd.DataFrame(
    {"company":["Hyundai","Nissan","Renault"],
     "model":["Kona","Leaf","Zoe"],
     "price":[154999,164800,125999]})
#add custom label to index
df.index = ["First","Second","Third"]
print(df)
