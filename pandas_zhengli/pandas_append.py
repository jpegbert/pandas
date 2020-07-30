import pandas as pd
import numpy as np

# https://www.cnblogs.com/guxh/p/9451532.html

df1 = pd.DataFrame(np.random.random((3, 3)), columns=list("ABC"))
df2 = pd.DataFrame(np.random.random((1, 3)), columns=list("ABC"))
df3 = pd.DataFrame(np.random.random((2, 3)), columns=list("ABC"))
print(df1)
print(df2)
print(df3)

result = df1.append(df2) # append只能按列合并
print(result)

# ignore_index
result = df1.append(df2, ignore_index=True)
print(result)

# append多个dataframe
result = df1.append([df2, df3], ignore_index=True)
print(result)

