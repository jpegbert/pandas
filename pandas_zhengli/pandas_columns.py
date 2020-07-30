import pandas as pd

# https://blog.csdn.net/th_num/article/details/80296254


df = pd.DataFrame([[1, 2, 3]], columns=list("ABC"))
# print(df)

# 最常用的方法
col = df.columns # 获取到的col是<class 'pandas.core.indexes.base.Index'>
# print(col)
# print(type(col))

# 获取数组类型的结果
col = df.columns.values
# print(col)
# print(type(col))

# 获取列表类型的结果
col = df.columns.values.tolist() # 方法1
print(col)
print(type(col))
col = df.columns.tolist() # 方法2
print(col)
print(type(col))
col = [column for column in df] # 方法3
print(col)
print(type(col))
col = list(df.columns.values) # 方法4
print(col)
print(type(col))
col = list(df)
print(col)
print(type(col))
col = list(df.columns)
print(col)
print(type(col))

