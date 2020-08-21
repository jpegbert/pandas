
# https://blog.csdn.net/castinga3t/article/details/79075240

import pandas as pd

path = 'F:/python/python数据分析与挖掘实战/图书配套数据、代码/chapter3/demo/data/catering_fish_congee.xls'
data = pd.read_excel(path, header=None, index_col=0)
data.index.name = '日期'
data.columns = ['销售额(元)']

xse = data['销售额(元)']
print(xse.max())
print(xse.min())
print(xse.max() - xse.min())

fanwei = list(range(0, 4500, 500))
fenzu = pd.cut(xse.values, fanwei, right=False)  # 分组区间,长度91
print(fenzu.codes)  # 标签
print(fenzu.categories)  # 分组区间，长度8
pinshu = fenzu.value_counts()  # series,区间-个数
print(pinshu.index)

import matplotlib.pyplot as plt

pinshu.plot(kind='bar')
# plt.text(0,29,str(29))


qujian = pd.cut(xse, fanwei, right=False)
data['区间'] = qujian.values
data.groupby('区间').median()
data.groupby('区间').mean()  # 每个区间平均数

pinshu_df = pd.DataFrame(pinshu, columns=['频数'])
pinshu_df['频率f'] = pinshu_df / pinshu_df['频数'].sum()
pinshu_df['频率%'] = pinshu_df['频率f'].map(lambda x: '%.2f%%' % (x * 100))

pinshu_df['累计频率f'] = pinshu_df['频率f'].cumsum()
pinshu_df['累计频率%'] = pinshu_df['累计频率f'].map(lambda x: '%.4f%%' % (x * 100))

print(pinshu_df)
