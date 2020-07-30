import pandas as pd
import numpy as np

# pandas显示不全
# https://blog.csdn.net/dpengwang/article/details/86483977
# https://blog.csdn.net/dpengwang/article/details/86483977
# https://blog.csdn.net/qq1195365047/article/details/89518826
# https://blog.csdn.net/qq_32146369/article/details/89214119

df = pd.DataFrame(np.random.random((100, 100)), columns=list(range(100)))

# 显示的最大行数，避免只显示部分行数据
pd.set_option('display.max_rows', 100)
# 显示的最大列数，避免列显示不全
pd.set_option('display.max_columns', 100)
# 每一列最大的宽度，避免属性值或列名显示不全
pd.set_option("display.max_colwidth", 100)
# 每一行的宽度，避免换行
pd.set_option('display.width', 100)

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# 一次写全
pd.set_option("display.max_rows", 100,
              "display.max_columns", 100,
              "display.max_colwidth", 100,
              "display.width", 100)
print(df)
