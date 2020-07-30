import pandas as pd


def method1():
    df = pd.read_csv("../data/train_city_23.csv", iterator=True)
    print(type(df)) # <class 'pandas.io.parsers.TextFileReader'>
    # 每执行一次，读取1000条数据，每次从上次读取结束的位置继续读取
    data = df.read(1000)
    print(type(data)) # <class 'pandas.core.frame.DataFrame'>
    print(data.shape)


def method2():
    df = pd.read_csv("../data/train_city_23.csv", chunksize=1000)
    print(type(df)) # <class 'pandas.io.parsers.TextFileReader'>
    for chunk in df:
        print(type(chunk)) # <class 'pandas.core.frame.DataFrame'>
        print(chunk.head())


def main():
    method1() # 方法1
    # method2() # 方法2


if __name__ == '__main__':
    main()

