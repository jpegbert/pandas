import pandas as pd


df = pd.DataFrame({'A': [3, 4, 8, 9],
                   'B': [1.2, 2.4, 4.5, 7.3],
                   'C': ["aa", "bb", "cc", "dd"]})
print(df)

print(df.describe()) # 查看数据值列的汇总统计, 字符串类型的列不会显示
print(df.mean()) # 查看数值列的平均值，字符串类型的列不会统计
print(df.corr()) # 返回数值列之间的相关系数
print(df.count()) # 返回每一列中的非空值的个数
print(df.max()) # 返回每一列的最大值
print(df.min()) # 返回每一列的最小值
print(df.median()) # 返回每一列的中位数
print(df.std()) # 返回每一数值列的标准差
print(df.sum()) # 返回每一列的总和
print(df.isnull().sum()) # 统计每列空值的数量
