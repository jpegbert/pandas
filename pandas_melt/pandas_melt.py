import pandas as pd

"""
pandas.melt 由 宽数据 变成 长数据

pandas.melt 使用参数：
pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
参数解释：
frame:要处理的数据集。
id_vars:不需要被转换的列名。
value_vars:需要转换的列名，如果剩下的列全部都要转换，就不用写了。
var_name和value_name是自定义设置对应的列名。
col_level :如果列是MultiIndex，则使用此级别。

https://blog.csdn.net/maymay_/article/details/80039677
"""


def main():
    d = {'col1': ['a', 'a', 'a', 'b', 'b'], 'col2': [1, 2, 3, 4, 5], 'col3': ['c', 'c', 'c', 'd', 'd']}
    df = pd.DataFrame(data=d)
    print(df)
    # col2是不需要转换的列，col1和col3被合并成了一列
    df1 = pd.melt(df, id_vars=['col2'])
    print(df1)

    # 设置 id_vars=['col2'],value_vars=['col1']，则不需要转换的列是col2。需要转换的是 col1列 ，拿col3 就不受影响，不展示了。
    df2 = pd.melt(df, id_vars=['col2'], value_vars=['col1'])
    print(df2)

    # 对修改后的列设置新列名。
    df3 = pd.melt(df, id_vars=['col2'], value_vars=['col1'], var_name='hi', value_name='hello')
    print(df3)
    df4 = pd.melt(df, id_vars=['col2'], var_name='hi', value_name='hello')
    print(df4)


if __name__ == '__main__':
    main()
