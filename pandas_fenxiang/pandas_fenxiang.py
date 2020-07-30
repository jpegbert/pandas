# https://blog.csdn.net/qq_41080850/article/details/88806989

import pandas as pd

"""
pandas 连续数据分箱
"""

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32, 22]   # 待分箱数据
bins = [18, 25, 35, 60, 100]   # 指定箱子的分界点

cats1 = pd.cut(ages, bins)
print("=====")
print(cats1)
print("=====")


# labels参数为False时，返回结果中用不同的整数作为箱子的指示符
cats2 = pd.cut(ages, bins,labels=False)
print(cats2)

print(pd.value_counts(cats1))   # 对不同箱子中的数进行计数

# 指定分箱区间是左闭右开, labels=False返回label数组
cats3 = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
print(cats3)


# 可以将想要指定给不同箱子的标签传递给labels参数
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cuts4 = pd.cut(ages, bins, labels=group_names)
print(cuts4)

qcats1 = pd.qcut(ages,q=4) # , labels=False返回箱子编号 # 参数q指定所分箱子的数量
print("=====")
print(qcats1)
print(qcats1.value_counts())  # 从输出结果可以看到每个箱子中的数据量是相同的
