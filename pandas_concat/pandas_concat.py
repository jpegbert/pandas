import pandas as pd
import numpy as np


# https://www.cnblogs.com/guxh/p/9451532.html

df1 = pd.DataFrame(np.ones((4, 4))*1, columns=list('DCBA'), index=list('4321'))
df2 = pd.DataFrame(np.ones((4, 4))*2, columns=list('FEDC'), index=list('6543'))
df3 = pd.DataFrame(np.ones((4, 4))*3, columns=list('FEBA'), index=list('6521'))

result = pd.concat([df1, df2])
print(result)
print("*" * 30)

# axis=0：竖方向（index）合并，合并方向index作列表相加，非合并方向columns取并集
result = pd.concat([df1, df2], axis=0)
print(result)
print("*" * 30)

# axis=1：横方向（columns）合并，合并方向columns作列表相加，非合并方向index取并集
result = pd.concat([df1, df2], axis=1)
print(result)
print("*" * 30)

# 合并方向是否忽略原行/列名称，而采用系统默认的索引，即从0开始的int。
# axis=0时ignore_index=True，index采用系统默认索引：
result = pd.concat([df1, df2], axis=0, ignore_index=True)
# axis=1时ignore_index=True，columns采用系统默认索引：
result = pd.concat([df1, df2], axis=1, ignore_index=True)


# 默认值：join_axes=None，取并集
# 合并后，可以设置非合并方向的行/列名称，使用某个df的行/列名称
# axis=0时join_axes=[df1.columns]，合并后columns使用df1的：
result = pd.concat([df1, df2], axis=0, join_axes=[df1.columns])
# axis=1时axes=[df1.index]，合并后index使用df2的：
result = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
# 同时设置join和join_axes的，以join_axes为准：
result = pd.concat([df1, df2], axis=0, join='inner', join_axes=[df1.columns])

# concat多个DataFrame
result = pd.concat([df1, df2, df3], sort=False, join_axes=[df1.columns])

