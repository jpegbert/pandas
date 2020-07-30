import pandas as pd
import numpy as np


df = pd.DataFrame([[2, 3], [3, 4]], columns=list("AB"))
# print(df)

# 对A列做log(x + 1)
# df["A"] = df["A"].apply(np.log1p) # np.log1p与np.expm1互为逆运算
# print(df)

# 对A列执行函数e的x次幂-1
# df["A"] = df["A"].apply(np.expm1) # np.log1p与np.expm1互为逆运算
# print(df)

# 对A列求e的次数幂
# df["A"] = df["A"].apply(np.exp) # np.exp与np.log互为逆运算
# print(df)

# 对A列取对数
# df["A"] = df["A"].apply(np.log) # np.exp与np.log互为逆运算
# print(df)

# 对A列开平方
# df["A"] = df["A"].apply(np.sqrt)
# print(df)

# 对A列计算平方
# df["A"] = df["A"].apply(np.exp2) # np.exp2与np.log2互为逆运算
# print(df)

# 对A列计算以2为底的对数
df["A"] = df["A"].apply(np.log2) # np.exp2与np.log2互为逆运算
print(df)

