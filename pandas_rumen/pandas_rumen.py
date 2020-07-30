import numpy as np
import pandas as pd


def creat_object():
    # 通过传入一些值的列表来创建一个Series，Pandas会自动创建一个默认的整数索引：
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

    # 通过传递带有日期时间索引和带标签列的NumPy数组来创建DataFrame：
    dates = pd.date_range('20130101', periods=6)
    print(dates)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)

    # 通过传递可以转化为类似Series的dict对象来创建DataFrame:
    df2 = pd.DataFrame({'A': 1.,'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]), 'F': 'foo'})
    print(df2)
    print(df2.dtypes)

    return df, dates


def look_dataframe(df):
    print("===================")
    print(df.head())
    print(df.tail(3))
    print("索引index:", df.index)
    print("列columns:", df.columns)
    # print(df.to_numpy()) # 报错
    print("汇总描述df.describe():", df.describe())
    print("转置df.T:", df.T)
    print("按轴排序df.sort_index:", df.sort_index(axis=1, ascending=False))
    print("按值排序df.sort_values:", df.sort_values(by='B'))


def select(df, dates):
    print("选择一列")
    print(df.A) # 选择一个列，产生一个“Series”
    print(df['A']) # 选择一个列，产生一个“Series”，相当于“df.A”：

    print("切片")
    print(df[0:3]) # 通过[]选择，对行进行切片：

    print("通过标签获取一行数据")
    print(df.loc[dates[0]])

    print("通过标签在多个轴上选择数据")
    print(df.loc[:, ['A', 'B']])

    print("通过标签同时在两个轴上切片")
    print(df.loc['20130102':'20130104', ['A', 'B']])
    print(df.loc['20130102', ['A', 'B']])

    print("获取标量值")
    print(df.loc[dates[0], 'A'])
    print("快速访问标量(和上面的方法效果相同)")
    print(df.at[dates[0], 'A'])

    print("通过传递的整数的位置选择")
    print(df.iloc[3])

    print("通过整数切片，类似于numpy/Python")
    print(df.iloc[3:5, 0:2])

    print("通过传递整数的列表按位置切片，类似于numpy/Python")
    print(df.iloc[[1, 2, 4], [0, 2]])

    print("整行切片")
    print(df.iloc[1:3, :])

    print("整列切片")
    print(df.iloc[:, 1:3])

    print("获取具体值")
    print(df.iloc[1, 1])
    print("快速访问标量(等价于之前的方法)")
    print(df.iat[1, 1])


def bool_index(df):
    print("使用单个列的值来选择数据")
    print(df[df.A > 0])

    print("从满足布尔条件的DataFrame中选择值")
    print(df[df > 0])

    print("使用 isin() 方法过滤")
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    print(df2[df2['E'].isin(['two', 'four'])])


def fuzhi(df, dates):
    print("添加新列将自动根据索引对齐数据")
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
    print(s1)
    df['F'] = s1
    print(df)

    print("通过标签赋值")
    df.at[dates[0], 'A'] = 0
    print(df)

    print("通过位置赋值")
    df.iat[0, 1] = 0
    print(df)

    print("使用NumPy数组赋值")
    df.loc[:, 'D'] = np.array([5] * len(df))
    print(df)

    print("带有where条件的赋值操作")
    df2 = df.copy()
    df2[df2 > 0] = -df2
    print(df2)


def queshizhi(df, dates):
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    df1.loc[dates[0]:dates[1], 'E'] = 1
    print(df1)

    print("删除任何带有缺失值的行")
    df2 = df1.dropna(how='any')
    print(df2)

    print("填充缺失值")
    df3 = df1.fillna(value=5) # 写成 df1.fillna(value=5, inplace=True) 会直接修改df1
    print(df3)

    print("获取值为nan的掩码")
    print(pd.isna(df1))

    print("统计dataframe中nan的数量")
    print(pd.isna(df1).sum())

    print("统计dataframe中某一列nan的数量")
    print(pd.isna(df1['E']).sum())


def caozuo(df, dates):
    print("进行描述性统计")
    print(df.mean())

    print("在其它轴(行)上进行同样的操作")
    print(df.mean(1))

    print("使用具有不同维度且需要对齐的对象进行操作。 此外，Pandas会自动沿指定维度进行广播")
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
    print(s)

    print(df.sub(s, axis='index'))


def apply(df, dates):
    print("将函数应用于数据")
    print(df.apply(np.cumsum))
    print(df.apply(lambda x: x.max() - x.min()))


def zhifanghuatu():
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s)
    print(s.value_counts())


def string():
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print(s.str.lower())


def merge():
    print("使用concat")
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)
    pieces = [df[:3], df[3:7], df[7:]]
    df2 = pd.concat(pieces)
    print(df2)


def merge1():
    left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    print("left")
    print(left)
    print("right")
    print(right)

    print("merge")
    df1 = pd.merge(left, right, on='key')
    print(df1)

    left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
    print("left")
    print(left)
    print("right")
    print(right)
    df1 = pd.merge(left, right, on='key')
    print(df1)


def append():
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    print(df)
    s = df.iloc[3]
    df2 = df.append(s, ignore_index=True)
    print(df2)


def grouping():
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8), 'D': np.random.randn(8)})
    print(df)
    df2 = df.groupby('A').sum()
    print(df2)

    df3 = df.groupby(['A', 'B']).sum()
    print(df3)


def stack():
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']]))
    print(tuples)
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    print(index)
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print(df)
    df2 = df[:4]
    print(df2)
    print("stacked")
    stacked = df2.stack()
    print(stacked)
    print("unstacked")
    print(stacked.unstack())
    print(stacked.unstack(1))
    print(stacked.unstack(0))


def pivot_tables(): # 数据透视表
    df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                       'B': ['A', 'B', 'C'] * 4,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D': np.random.randn(12),
                       'E': np.random.randn(12)})
    print(df)
    df1 = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
    print(df1)


def time_series():
    rng = pd.date_range('1/1/2012', periods=100, freq='S')
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)


def categoricals():
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                       "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    # 将原始成绩转换为category数据类型
    df["grade"] = df["raw_grade"].astype("category")
    print(df)
    # 将类别重命名为更有意义的名称(通过调用Series.cat.categories来替换！)
    df["grade"].cat.categories = ["very good", "good", "very bad"]
    print(df)
    # 对categories重新排序并同时添加缺少的category(Series.cat下的方法默认返回一个新的Series)
    df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
    print(df["grade"])
    print(df.sort_values(by="grade"))
    # 按分好类的列分组(groupby)可以显示空categories
    size = df.groupby("grade").size()
    print(size)


def plot():
    ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()

    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns = ['A', 'B', 'C', 'D'])
    df = df.cumsum()
    # plt.figure()
    # df.plot()
    # plt.legend(loc='best')


def input_output():
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                       "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    df.to_csv('foo.csv') # 写入csv
    pd.read_csv('foo.csv') # 从csv读取
    df.to_hdf('foo.h5', 'df') # 写入HDF5
    pd.read_hdf('foo.h5', 'df') # 从HDF5读数据
    df.to_excel('foo.xlsx', sheet_name='Sheet1') # 写入excel文件
    pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']) # 从Excel文件读取数据


def main():
    df, dates = creat_object() # 创建对象
    look_dataframe(df) # 查看对象
    select(df, dates) # 选择
    bool_index(df) # 布尔索引
    fuzhi(df, dates) # 赋值
    queshizhi(df, dates) # 缺失值
    caozuo(df, dates) # 操作
    apply(df, dates) # 应用
    zhifanghuatu() # 直方画图
    string() # 字符串方法
    merge() # 合并
    merge1() # merge
    append() # 追加
    grouping() # 分组
    # reshaping() # 重塑
    stack() # 堆叠
    pivot_tables() # 数据透视表(PivotTables)
    time_series() # 时间序列(TimeSeries)
    categoricals() # 分类(Categoricals)
    plot() # 绘图
    input_output() # 读文件和写文件


if __name__ == '__main__':
    main()

