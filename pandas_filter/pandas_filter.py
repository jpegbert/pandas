import pandas as pd


# https://www.cnblogs.com/beyondChan/p/10861045.html


df = pd.DataFrame({'A': [100, 200, 300, 400, 500],
                   'B': ['a', 'b', 'c', 'd', 'e'],
                   'C': [1, 2, 3, 4, 5]})

# 找出df中A列值为100的所有数据
print(df[df.A == 100])
# 也可以采用
print(df[df["A"] == 100])
# 注意：上面也可以是小于（<）、大于（>）、小于等于（<=）、大于等于（>=）、不等于（!=）等情况

# 找出df中A列值为100、200、300的所有数据
num = [100, 200, 300]
# 筛选出A列值在num列表的数据条
print(df[df.A.isin(num)])
# 也可以写成下面的形式
print(df[df["A"].isin(num)])

# 找出df中A列值为100且B列值为‘a’的所有数据
print(df[(df.A == 100) & (df.B == 'a')])
# 也可以采用下面的形式
print(df[(df["A"] == 100) & (df["B"] == 'a')])

# 找出df中A列值为100或B列值为‘b’的所有数据
print(df[(df.A == 100) | (df.B == 'b')])
# 也可以采用下面的形式
print(df[(df["A"] == 100) | (df["B"] == 'b')])

