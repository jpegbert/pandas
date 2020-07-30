import pandas as pd
import numpy as np

# https://www.cnblogs.com/guxh/p/9451532.html

df1 = pd.DataFrame(np.random.random((3, 3)), columns=list("ABC"))
df2 = pd.DataFrame(np.random.random((1, 3)), columns=list("ABD"))
df3 = pd.DataFrame(np.random.random((2, 3)), columns=list("ABC"))

print(df1)
print(df2)
print(df3)

# 省略axis，默认axis=0，沿着列方向合并，非合并方向columns取并集
# 省略ignore_index，默认索引值不相加，即保留原来的索引
result = pd.concat([df1, df2])
print(result)

# 按列合并
# axis=0：竖方向（index）合并，合并方向index作列表相加，非合并方向columns取并集
result = pd.concat([df1, df2], axis=0)
print(result)

# 按行合并
# axis=1：横方向（columns）合并，合并方向columns作列表相加，有相同的列，也都保留，非合并方向index取并集
result = pd.concat([df1, df2], axis=1)
print(result)

# 索引合并方式
# 合并方向是否忽略原行/列名称，而采用系统默认的索引，即从0开始的int
# axis=0时ignore_index=True，index采用系统默认索引：
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)
# axis=1时ignore_index=True，columns采用系统默认索引：
result = pd.concat([df1, df2], axis=1, ignore_index=True)
print(result)

# 指定合并后的列
# cancat默认合并后的列是要合并的dataframe的并集，可以采用属性join_axes设置合并后的列名和索引。
# 默认join_axes=None，axis=0时，按竖直方向合并，设置join_axes=[df1.columns]，表示合并后columns使用df1的
result = pd.concat([df1, df2], axis=0, join_axes=[df1.columns])
print(result)
# axis=1时，按水平方向合并，设置join_axes=[df1.index]，合并后index使用df1的：
result = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(result)

# join参数 inner，相同列必须完全相同，相当于取交集（join的参数值不可以是left和right）
result = pd.concat([df1, df2], axis=1, join='inner')
print(result)
# join参数 outer，会保留所有列，相当于取并集
result = pd.concat([df1, df2], axis=1, join='outer')
print(result)

# 同时设置join和join_axes的，以join_axes为准
result = pd.concat([df1, df2], axis=0, join='inner', join_axes=[df1.columns])
print(result)

# concat多个DataFrame
result = pd.concat([df1, df2, df3], sort=False, join_axes=[df1.columns], ignore_index=True)
print(result)
