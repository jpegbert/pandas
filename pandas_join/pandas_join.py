# https://www.cnblogs.com/xk-bench/p/8379180.html
from pandas import Series, DataFrame, merge

data = DataFrame([{"id": 0, "name": 'lxh', "age": 20, "cp": 'lm'}, {"id": 1, "name": 'xiao', "age": 40, "cp": 'ly'},
                  {"id": 2, "name": 'hua', "age": 4, "cp": 'yry'}, {"id": 3, "name": 'be', "age": 70, "cp": 'old'}],
                 index=['a', 'b', 'c', 'd'])
data1 = DataFrame([{"sex": 0}, {"sex": 1}, {"sex": 2}], index=['a', 'b', 'e'])

print("data")
print(data)

print("data1")
print(data1)

print('使用默认的左连接\r\n', data.join(data1))  # 这里可以看出自动屏蔽了data中没有的index=e 那一行的数据
# print('使用右连接\r\n', data.join(data1, how="right"))  # 这里出自动屏蔽了data1中没有index=c,d的那行数据；等价于data1.join(data)
# print('使用内连接\r\n', data.join(data1, how='inner'))
# print('使用全外连接\r\n', data.join(data1, how='outer'))
# print('使用左连接\r\n', data.join(data1, how='left'))
