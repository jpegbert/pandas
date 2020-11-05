# https://blog.csdn.net/MsSpark/article/details/83154128

import numpy as np
import pandas as pd
df = pd.DataFrame({'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
                   'col2': [2, 1, 9, 8, 7, 7],
                   'col3': [0, 1, 9, 4, 2, 8]})
print(df)
print("=" * 10)

# 依据第一列排序，并将该列空值放在首位
df1 = df.sort_values(by=['col1'], na_position='first', inplace=False)
print(df1)
print("=" * 10)

# 依据第二、三列，数值降序排序
df2 = df.sort_values(by=['col2', 'col3'], ascending=False, inplace=False)
print(df2)
print("=" * 10)

# 根据第一列中数值排序，按降序排列，并替换原数据
df.sort_values(by=['col1'], ascending=False, na_position='first', inplace=True)
print(df)
print("=" * 10)

x = pd.DataFrame({'x1': [1, 2, 2, 3], 'x2': [4, 3, 2, 1], 'x3': [3, 2, 4, 1]})
print(x)
# 按照索引值为0的行，即第一行的值来降序排序
print(x.sort_values(by=0, ascending=False, axis=1))
