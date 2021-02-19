import pandas as pd
import numpy as np


"""
https://zhuanlan.zhihu.com/p/100064394

applymap的用法比较简单，会对DataFrame中的每个单元格执行指定函数的操作
"""


df = pd.DataFrame(
    {
        "A": np.random.randn(5),
        "B": np.random.randn(5),
        "C": np.random.randn(5),
        "D": np.random.randn(5),
        "E": np.random.randn(5),
    }
)
print(df)

df = df.applymap(lambda x: "%.2f" % x)
print(df)
