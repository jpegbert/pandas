import pandas as pd
import random

# https://blog.csdn.net/tz_zs/article/details/88044920


df = pd.DataFrame()
df["col1"] = [10, None, 12, None, 14, 15, 16]
df.index = list("abcdefg")
# random.shuffle 打乱
df["col3"] = df["col1"]
random.shuffle(df["col3"])
print(df)
"""
   col1  col3
a  10.0   NaN
b   NaN  15.0
c  12.0  10.0
d   NaN  12.0
e  14.0  16.0
f  15.0   NaN
g  16.0  14.0
"""

df[["r_t_keep"]] = df[["col3"]].rank(axis=0, na_option="keep", ascending=True)
df[["r_t_top"]] = df[["col3"]].rank(axis=0, na_option="top", ascending=True)
df[["r_t_bottom"]] = df[["col3"]].rank(axis=0, na_option="bottom", ascending=True)
df[["r_f_keep"]] = df[["col3"]].rank(axis=0, na_option="keep", ascending=False)
df[["r_f_top"]] = df[["col3"]].rank(axis=0, na_option="top", ascending=False)
df[["r_f_bottom"]] = df[["col3"]].rank(axis=0, na_option="bottom", ascending=False)
print(df)
"""
   col1  col3  r_t_keep  r_t_top  r_t_bottom  r_f_keep  r_f_top  r_f_bottom
a  10.0   NaN       NaN      1.5         6.5       NaN      1.5         6.5
b   NaN  15.0       4.0      6.0         4.0       2.0      4.0         2.0
c  12.0  10.0       1.0      3.0         1.0       5.0      7.0         5.0
d   NaN  12.0       2.0      4.0         2.0       4.0      6.0         4.0
e  14.0  16.0       5.0      7.0         5.0       1.0      3.0         1.0
f  15.0   NaN       NaN      1.5         6.5       NaN      1.5         6.5
g  16.0  14.0       3.0      5.0         3.0       3.0      5.0         3.0
"""
