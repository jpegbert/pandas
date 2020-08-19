# https://blog.csdn.net/u012706792/article/details/80892510
import pandas as pd
# import numpy as np
#
# np.median

df = pd.DataFrame({'Country': ['China', 'China', 'India', 'India', 'America', 'Japan', 'China', 'India'],
                   'Income': [10000, 10000, 5000, 5002, 40000, 50000, 8000, 5000],
                   'Age': [5000, 4321, 1234, 4010, 250, 250, 4500, 4321]})

print(df)
print("=======单列分组========")
df_gb = df.groupby('Country')
for index, data in df_gb:
    print(index)
    print(data)

print("-" * 20)
print(df)
print("=======多列分组========")
df_gb = df.groupby(['Country', 'Income'])
for (index1, index2), data in df_gb:
    print((index1, index2))
    print(data)

print("=======对分组后数据进行聚合========")
df_agg = df.groupby('Country').agg(['min', 'mean', 'max', 'sum'])
print(df_agg)

print("=======对分组后的部分列进行聚合========")
# num_agg = {'Age': ['min', 'mean', 'max', 'sum']}
num_agg = {'Age': 'mean', 'Age': 'sum', 'Income': 'sum'} # 这种写法，agg之后不会出现聚合的lie有两个索引的情况
# 参数as_index表示是否以分组的列作为as_index=False索引, 默认是分组的列作为索引的
print(df)
print("*" * 20)
df2 = df.groupby('Country', as_index=False).agg(num_agg)
print(df2)

print("&&" * 10)
print(df2.columns)

# df2.reset_index(drop=True)
# age = df2[df2['Country']=='China'].Age.iloc[0]
# print("------")
# print(type(age))
# print(age)

