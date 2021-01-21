import pandas as pd

# https://blog.csdn.net/qq_38038143/article/details/102624344
# https://blog.csdn.net/asher117/article/details/103786900


data_dict = {"name": ["Rose", "Jack", "Tom", "Kyle", "Jery", "Adam", "Bill", "David", "Denny", "Evan"],
             "class": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],
             "score": [88, 92, 38, 98, 22, 65, 45, 53, 97, 100]}
df = pd.DataFrame(data=data_dict)
print(df)

df['rank'] = df['score'].groupby(df['class']).rank()
df = df.sort_values(by=["class", "rank"], axis=0, ascending=False)
print(df)
