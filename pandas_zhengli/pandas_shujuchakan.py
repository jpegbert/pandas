import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.random((4, 3)), columns=list("ABC"))
print(df)

# 查看前n行
result = df.head(2)
print(result)

# 查看最后n行
result = df.tail(2)
print(result)

# 查看行数和列数
result = df.shape
print(result)
print(type(result))

# 查看索引，数据类型等信息
result = df.info()
print(result)

# 查看数值列的汇总统计
result = df.describe()
print(result)

# 查看某一列的唯一值计数
result = df["A"].value_counts(dropna=False)
print(result)

# 查看DataFrame对象中每一列的唯一值和计数
result = df.apply(pd.Series.value_counts)
print(result)

