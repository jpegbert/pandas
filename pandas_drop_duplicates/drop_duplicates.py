# https://blog.csdn.net/jasonwang_/article/details/78984852

import pandas as pd


data={'state':[1,1,2,2,1,2,2],'pop':['a','b','c','d','b','c','d']}
frame = pd.DataFrame(data)
print("原始数据")
print(frame)

a = frame.drop_duplicates(subset=['pop'],keep='first') # 去除重复列, 保留第一个
print("==========")
print(a)

b = frame.drop_duplicates(subset=['pop'],keep=False) # 去除重复列, 保留无重复的
print("==========")
print(b)

a.append(b).drop_duplicates(subset=['pop'],keep=False)
print("==========")
print(a)




