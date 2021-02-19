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
a    10    20    15    20
b    11    21    14    24
c    12    21    13    21
d    13    22    11    21
e    14    23    10    25
f    15    24    12    23
g    16    25    16    22
"""
df[["r_average"]] = df[["col4"]].rank(axis=0, method="average")
df[["r_min"]] = df[["col4"]].rank(axis=0, method="min")
df[["r_max"]] = df[["col4"]].rank(axis=0, method="max")
df[["r_first"]] = df[["col4"]].rank(axis=0, method="first", ascending=False)
df[["r_dense"]] = df[["col4"]].rank(axis=0, method="dense")
print(df)
"""
   col1  col2  col3  col4  r_average  r_min  r_max  r_first  r_dense
a    10    20    15    20        1.0    1.0    1.0      1.0      1.0
b    11    21    14    24        6.0    6.0    6.0      6.0      5.0
c    12    21    13    21        2.5    2.0    3.0      2.0      2.0
d    13    22    11    21        2.5    2.0    3.0      3.0      2.0
e    14    23    10    25        7.0    7.0    7.0      7.0      6.0
f    15    24    12    23        5.0    5.0    5.0      5.0      4.0
g    16    25    16    22        4.0    4.0    4.0      4.0      3.0
"""

