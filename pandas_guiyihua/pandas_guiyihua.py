# https://blog.csdn.net/hjxzb/article/details/78610961

import numpy as np
import pandas as pd

np.random.seed(1)
df = pd.DataFrame(np.random.randn(4, 4) * 4 + 3)
df.columns = ['a', 'b', 'c', 'd']
# df.columns = ['color', 'size', 'prize', 'class label']
print(df)
"""
          0         1         2         3
0  9.497381  0.552974  0.887313 -1.291874
1  6.461631 -6.206155  9.979247 -0.044828
2  4.276156  2.002518  8.848432 -5.240563
3  1.710331  1.463783  7.535078 -1.399565

"""
# print("----")
# print(df.min())
# print("----")
# print(df.max())
# print("----")
df_norm = (df - df.min()) / (df.max() - df.min())
print(df_norm)
print("----")
norm_cols = ['a', 'b']
df_norm_cols = (df[norm_cols] - df[norm_cols].min()) / (df[norm_cols].max() - df[norm_cols].min())
print(df_norm_cols)
print("----")
df.drop(['a', 'b'], axis=1, inplace=True)
df_final = df_norm_cols.join(df)
print(df_final)
"""
          0         1         2         3
0  1.000000  0.823413  0.000000  0.759986
1  0.610154  0.000000  1.000000  1.000000
2  0.329499  1.000000  0.875624  0.000000
3  0.000000  0.934370  0.731172  0.739260
"""
# df_norm2 = df.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
# print(df_norm2)

