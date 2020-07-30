import pandas as pd
import numpy as np

# https://www.cnblogs.com/guxh/p/9451532.html

df1 = pd.DataFrame(np.ones((4, 4))*1, columns=list('DCBA'), index=list('4321'))
df2 = pd.DataFrame(np.ones((4, 4))*2, columns=list('FEDC'), index=list('6543'))
df3 = pd.DataFrame(np.ones((4, 4))*3, columns=list('FEBA'), index=list('6521'))

result = df1.append(df2) # 相当于pd.concat([df1, df2])
print(result)
print("*" * 30)

result = df1.append(df2, ignore_index=True) # ignore_index
print(result)
print("*" * 30)

result = df1.append([df2, df3], ignore_index=True) # 和concat相同，append也支持append多个DataFrame
print(result)
print("*" * 30)
