# https://blog.csdn.net/qq_33873431/article/details/98077676
import pandas as pd
import numpy as np


def ndarray_to_series2(): # 如果是二维数组转换为Series
    data = np.array([1, 2, 3]).reshape(3, 1)
    data_list = map(lambda x: x[0], data) # 把二维数组转换成list
    ser = pd.Series(data_list)


def ndarray_to_series1(): # 如果是一维数组转换为Series
    data = np.array([1, 2, 3])
    ser = pd.Series(data.tolist())


def series_to_ndarray(): # series转换为ndarray。通过Series.values实现series转换为ndarray
    data = [['2019/08/01', 10],
            ['2019/08/01', 11]]
    result = pd.DataFrame(data, columns=['ds', 'val'])
    result['val'].values
    data2 = pd.Series([1, 2, 3])
    data2.values


def ndarray_to_df(): # ndarray转换为dataframe
    data = np.array([['2019/08/02', 'zhansan', 1], ['2019/08/03', 'lisi', 2], ['2019/08/04', 'wangwu', 3]])
    df = pd.DataFrame(data)


def ndarray_to_df1(): # 指定索引、数据、列名例子
    data = np.array([['', 'Col1', 'Col2'], ['Row1', 1, 2], ['Row2', 3, 4]])
    df = pd.DataFrame(data=data[1:, 1:],  # 从第2行开始并且第2列开始作为数据
                      index=data[1:, 0],  # 第1列做索引，从第2行开始
                      columns=data[0, 1:])  # 第1行作为列名，从第2列开始


def df_to_ndarray():
    # 通过values方法，实现dataframe转换为ndarray
    import pandas as pd
    data = [['2019/08/01', 10],
            ['2019/08/01', 11]]
    result = pd.DataFrame(data, columns=['ds', 'val'])
    result.values
    # 通过切片，实现某一行或者某一列转换为ndarray
    rs = result.values
    print(rs[:, 0])
    print(rs[0, :])


def main():
    # ndarray_to_series2()
    # ndarray_to_series1()
    # series_to_ndarray()
    # ndarray_to_df()
    # ndarray_to_df1()
    df_to_ndarray()


if __name__ == '__main__':
    main()
