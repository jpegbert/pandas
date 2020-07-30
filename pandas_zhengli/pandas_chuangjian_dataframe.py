import pandas as pd
import numpy as np


# https://www.cnblogs.com/datasnail/p/9675410.html
# https://www.pypandas.cn/docs/getting_started/10min.html#%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA


def create_from_dict(): # 从字典中创建df
    # 使用字典创建df, 字典的每一项采用不同的series创建方式
    df = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20191213'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'
                       })
    print(df)

    # 使用字典创建df, 字典中每一项的值是列表
    df = pd.DataFrame({'A': [3, 4, 8, 9], 'B': [1.2, 2.4, 4.5, 7.3], 'C': ["aa", "bb", "cc", "dd"]})
    print(df)


def create_from_np_array(): # 从numpy数组中创建df
    df = pd.DataFrame(np.random.randn(3, 3), columns=list("ABC"))
    print(df)


def create_from_list(): # 从嵌套列表中创建df
    df = pd.DataFrame([["12", "34", "56"], [1, 2, 3]], columns=["A", "B", "C"])
    print(df)


def main():
    create_from_dict() # 从字典中创建df
    create_from_np_array() # 从numpy数组中创建df
    create_from_list() # 从嵌套列表中创建df


if __name__ == '__main__':
    main()

