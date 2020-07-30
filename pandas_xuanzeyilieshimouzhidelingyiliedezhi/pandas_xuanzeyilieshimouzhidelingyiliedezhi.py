import pandas as pd


# 从dataframe中获得某一列是某值的另一列的值
# https://segmentfault.com/q/1010000013349234


df = pd.DataFrame({'A': [3, 4, 8, 9],
                   'B': [1.2, 2.4, 4.5, 7.3],
                   'C': ["aa", "bb", "cc", "dd"]})
print(df)

print(df.query('B==2.4').A.values[0]) # 第一种写法
print(df[df['B']==2.4]['A'].values[0]) # 第二种写法
print(df['A'][df['B']==2.4].values[0]) # 第三种写法

