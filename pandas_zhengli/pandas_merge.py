import pandas as pd


# https://www.cnblogs.com/guxh/p/9451532.html
# https://blog.csdn.net/Asher117/article/details/84725199


df1 = pd.DataFrame({'A': [3, 4, 8, 9],
                   'B': [1.2, 2.4, 4.5, 7.3],
                   'C': ["aa", "bb", "cc", "dd"]})
print(df1)
df2 = pd.DataFrame({'B': [1.2, 2.2, 4.3, 7.3],
                   'C': ["ab", "bb", "cc", "dd"],
                    'D':[1, 2, 3, 4]})
print(df2)


def merge_direct():  # 直接合并，采用默认的连接方式
    # 默认采用inner连接方式, 按照列名相同的列进行合并
    result = pd.merge(df1, df2)
    print(result)


def merge_on(): # 指定on参数, 以特定的列进行合并
    result = pd.merge(df1, df2, on='B')
    # 指定on，设定合并基准列，按照设置的列名称进行合并，并且两个
    # dataframe中除了on参数指定的列之外的共同列会同时变换名称后保留下来
    print(result)


def merge_how(): # 指定how属性
    # ‘inner’(默认)：共同列的值必须完全相等：
    result = pd.merge(df1, df2, on='B', how='inner')
    print("inner", result)

    # 'outer’共同列的值都会保留，两个dataframe在共同列上的差集，会对它们的缺失列项的值赋上NaN
    result = pd.merge(df1, df2, on='B', how='outer')
    print("outer", result)

    # ‘left’根据左边的DataFrame确定共同列的保留值，右边缺失列项的值赋上NaN
    result = pd.merge(df1, df2, on='B', how='left')
    print("left", result)

    # ‘right’根据右边的DataFrame确定共同列的保留值，左边缺失列项的值赋上NaN
    result = pd.merge(df1, df2, on='B', how='right')
    print("right", result)


def merge_by_muilty_cols(): # 指定多列合并
    result = pd.merge(df1, df2, on=['B', 'C'], how='inner')
    print(result)


def merge_left_on_and_right_on(): # 采用left_on 和 right_on对两个列名不同的dataframe合并
    result = pd.merge(df1, df2, left_on='A', right_on='D', how='inner')
    print(result)


def merge_index(): # 设置left_index或者right_index的值为True使用索引连接
    # df1的索引与df2的D列相同时合并
    result = pd.merge(df1, df2, left_index=True, right_on='D')
    print(result)


def merge_suffixes(): # 合并后对相同的列名重命名
    result = pd.merge(df1, df2, on='B', how='outer', suffixes=('_df1', '_df2'))
    print(result)


def main():
    # merge_direct()  # 直接合并，采用默认的连接方式
    # merge_on() # 指定on参数, 以特定的列进行合并
    # merge_how() # 指定how属性
    # merge_by_muilty_cols()  # 指定多列合并
    # merge_left_on_and_right_on() # 采用left_on 和 right_on对两个列名不同的dataframe合并
    # merge_index() # 设置left_index或者right_index的值为True使用索引连接
    merge_suffixes() # 合并后对相同的列名重命名


if __name__ == '__main__':
    main()
