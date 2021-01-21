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
a    10    20    13    21
b    11    21    16    21
c    12    21    12    22
d    13    22    15    24
e    14    23    11    23
f    15    24    10    25
g    16    25    14    20
"""
print(df.loc[["a", "b"]].rank(1))  # 列排名
"""
   col1  col2  col3  col4
a   1.0   3.0   2.0   4.0
b   1.0   3.5   2.0   3.5
"""
df[["rank1", "rank2"]] = df[["col3", "col4"]].rank(0)  # 行排名
print(df)
"""
   col1  col2  col3  col4  rank1  rank2
a    10    20    13    21    4.0    2.5
b    11    21    16    21    7.0    2.5
c    12    21    12    22    3.0    4.0
d    13    22    15    24    6.0    6.0
e    14    23    11    23    2.0    5.0
f    15    24    10    25    1.0    7.0
g    16    25    14    20    5.0    1.0
"""
