import pandas as pd


# https://www.jianshu.com/p/10d7fe75026c


df1 = pd.DataFrame([1,2,3,4,5])
print(id(df1)) # 4541269200

df2 = df1
print(id(df2)) # 4541269200  # 与df1一样的ID

df3 = df1.copy()
print(id(df3)) # 4541269584  # df3是个新的对象，有新的ID

df4 = df1.copy(deep=False) # 浅拷贝
print(id(df4)) # 4541269072  # 新的对象，有新的ID

df1 = pd.DataFrame([9, 9, 9])
print(id(df1)) # 4541271120  # 新对象，新的ID，捆绑在df1 的名字上
print(id(df2)) # 4541269200  # 旧的对象不受影响


"""
从上面的代码可以看出， = 过程是让新的变量指向旧变量的地址，两个变量指向同一个内容，改变这个内容，这两个变量都会改变。

copy() 和 copy(deep= False)都是浅拷贝，是复制了旧对象的内容，然后重新生成一个新对象，新旧对象的ID 是不同的，改变旧对象不会影响新对象。
浅拷贝是只拷贝父对象，不拷贝对象内部的子对象的

如果一个对象中还有list ， 就像 [1,2,3,4, ['lalala','hahaha'] ],那么copy只会拷贝第一层对象，对第二层['lalala','hahaha'] 的修改还是会反映到copy过的新对象中。
"""


import copy
t1 = [1, 2, [1, 2], 4, 5]
t2 = t1
t3 = t1.copy()
t4 = copy.deepcopy(t1)

t1[1] = '666'
t1.append([6, 7])
t1[2].append(3)

print("t1:", t1, id(t1)) # t1: [1, '666', [1, 2, 3], 4, 5, [6, 7]] 1621427166728 #用等号的两个变量ID一样
print("t2:", t2, id(t2)) # t2: [1, '666', [1, 2, 3], 4, 5, [6, 7]] 1621427166728 #用等号的两个变量ID一样
print("t3:", t3, id(t3)) # t3: [1, 2, [1, 2, 3], 4, 5] 1621427326664 # shallow copy创建了新ID,对第一级对象的修改不影响变量，但对第二级对象的修改还是会影响变量
print("t4:", t4, id(t4)) # t4: [1, 2, [1, 2], 4, 5] 1621422497480 #deep copy 也创建了新ID,且不会影响二级，三级等子对象


# 然而在dataframe里deep copy 是没用的，在pandas中没法深拷贝
