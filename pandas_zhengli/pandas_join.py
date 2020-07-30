import pandas as pd

# https://www.cnblogs.com/xk-bench/p/8379180.html

df1 = pd.DataFrame({'A': [3, 4, 8, 9], 'B': [1.2, 2.4, 4.5, 7.3], 'C': ["aa", "bb", "cc", "dd"]})
df2 = pd.DataFrame({'D': [1, 2]})
print(df1)
print(df2)

# 默认采用left的连接方式，索引相同时连接成一行
result = df1.join(df2)
print(result)

# 左连接
result = df1.join(df2, how='left')
print(result) # 可以看到与不写how完全一样

# 右连接
result = df1.join(df2, how='right')
print(result)

# 内连接
result = df1.join(df2, how='inner')
print(result)

# 全连接
result = df1.join(df2, how='outer')
print(result)


# join是按照索引进行连接，在实际应用中，常常需要采用下面这种方法临时设置索引
df3 = pd.DataFrame({'C': ['bb', 'dd'], 'D': [1, 2]})
print(df3)

# 此时，df1和df3有共同的列C，如果直接对df1和df3按照索引进行合并会报错
# result = df1.join(df3) # 报错: ValueError: columns overlap but no suffix specified
# 对于两个dataframe有共同列，且共同列不是连接列的时候，需要使用属性lsuffix和rsuffix指定相同列的后缀
result = df1.join(df3, lsuffix='_l', rsuffix='_r')
print(result)
#
# 按照C列进行合并, 可以通过参数how设置连接方式
result = df1.set_index("C").join(df3.set_index("C"), on="C", how="left")
print(result)
result = df1.set_index("C").join(df3.set_index("C"), on="C", how="right")
print(result)
result = df1.set_index("C").join(df3.set_index("C"), on="C", how="inner")
print(result)
result = df1.set_index("C").join(df3.set_index("C"), on="C", how="outer")
print(result)
# # 这样写完之后一般再恢复之前的索引
df1.reset_index(inplace=True)
df3.reset_index(inplace=True)
# 或者
df1 = df1.reset_index()
df3 = df3.reset_index()
