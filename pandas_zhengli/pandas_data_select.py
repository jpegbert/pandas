import pandas as pd


df = pd.DataFrame({'A': [3, 4, 8, 9],
                   'B': [1.2, 2.4, 4.5, 7.3],
                   'C': ["aa", "bb", "cc", "dd"]})
print(df)


def main():
    df1 = df['A'] # 根据列名选取一列，以Series的形式返回列
    df1 = df.A # 与上面写法效果相同
    # print(df1)
    # print(type(df1))  # <class 'pandas.core.series.Series'>
    #
    df1 = df[['A', 'B']] # 根据列名的列表，以DataFrame形式返回多列
    # print(df1)
    # print(type(df1)) # 返回<class 'pandas.core.frame.DataFrame'>
    #
    # print("=============")
    # print(df[0:2])  # 通过[]选择，对行进行切片，选择前三行
    #
    # print("==========")
    # print(df.iloc[0,:]) # 选择第一行
    #
    # print("=============")
    # print(df.iloc[0, 0]) # 选择第一行第一列的元素
    #
    # print("=============")
    # # 在多个轴上选择数据， 注意loc和at效果和用法相同
    # print(df.loc[:, ['B', 'C']])
    # print("=============")
    # print(df.loc[1:2, ['B', 'C']])
    # print(df.at[2, 'A']) # 获取第三行，'A'列的元素, at与loc的用法和效果相同
    #
    # print("通过传递的整数的位置选择")
    # print(df.iloc[2]) # 选择索引是2的行
    #
    # print("通过传递整数的列表按位置切片，类似于numpy/Python")
    # print(df.iloc[[1, 2], [0, 2]])
    #
    # print("整行切片")
    result = df.iloc[1:3, :]
    print(result) # 选择第2--3行的所有列
    #
    # print("整列切片")
    # print(df.iloc[:, 1:2]) # 选择第2--3列的所有行
    #
    # print("获取具体值")
    # print(df.iloc[1, 1])
    # print("快速访问标量(等价于之前的方法)")
    # print(df.iat[1, 1]) # 快速访问标量(等价于之前的方法)

    # print(df.loc[1:2, :])


if __name__ == '__main__':
    main()
