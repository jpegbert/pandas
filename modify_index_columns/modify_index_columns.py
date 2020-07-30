# https://blog.csdn.net/missyougoon/article/details/83780845
# https://blog.csdn.net/xxzhangx/article/details/76609925

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(9).reshape(3, 3), index = ['bj', 'sh', 'gz'], columns=['a', 'b', 'c'])
print(df1)
# df1['a'] = -1
# print(df1)

df1.index.name = 'city'
df1.columns.name = 'city'

print("===========")
print(df1)

df1.to_csv("./test.csv")
df2 = pd.read_csv("./test.csv")
print(df2)
print(df2['city'])



# print(df1.index)

