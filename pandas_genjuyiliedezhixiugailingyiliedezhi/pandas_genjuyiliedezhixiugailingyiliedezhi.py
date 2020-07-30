# 根据一列的值修改另一列的值
import pandas as pd


df = pd.DataFrame({'A': [3, 4, 8, 9],
                   'B': ["aa", "bb", "cc", "dd"]})
df.loc[df["A"]==4, 'A'] = "Test"
print(df)


