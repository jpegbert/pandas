import pandas as pd
import random

# https://blog.csdn.net/tz_zs/article/details/88044920


df = pd.DataFrame()
df["col1"] = [10, 11, 12, 13, 14, 15, 16]
df["col2"] = [20, 21, 21, 22, 23, 24, 25]
df.index = list("abcdefg")
# random.shuffle 打乱
df["col3"] = df["col1"]
df["col4"] = df["col2"]
random.shuffle(df["col3"])
random.shuffle(df["col4"])
print(df)
"""
   col1  col2  col3  col4
a    10    20    15    22
b    11    21    11    21
c    12    21    13    21
d    13    22    10    23
e    14    23    16    20
f    15    24    12    25
g    16    25    14    24
"""
df[["r_1"]] = df[["col4"]].rank(axis=0, pct=False)
df[["r_2"]] = df[["col4"]].rank(axis=0, pct=True) # 达到类似求分位数的效果
print(df)
"""
   col1  col2  col3  col4  r_1       r_2
a    10    20    15    22  4.0  0.571429
b    11    21    11    21  2.5  0.357143
c    12    21    13    21  2.5  0.357143
d    13    22    10    23  5.0  0.714286
e    14    23    16    20  1.0  0.142857
f    15    24    12    25  7.0  1.000000
g    16    25    14    24  6.0  0.857143
"""
