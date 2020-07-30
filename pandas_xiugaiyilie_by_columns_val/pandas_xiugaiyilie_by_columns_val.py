import pandas as pd

data = pd.read_csv("C:/Users/pengjiang/Desktop/train_city_23.csv")

print(len(data))
data = data[:20]
print(len(data))
print(data.columns)
data["is_weekend"] = 0
# data.loc[data.weekday >= 6, "is_weekend"] = 1
data.at[data.weekday >= 6, "is_weekend"] = 1
print(data.head())

df = data[["weekday", "is_weekend"]]
print(df)
