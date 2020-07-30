import pandas as pd



def anhanghebing(): # 按行合并
    df1 = pd.DataFrame(0, columns=["a", "b"], index=range(5))
    df2 = pd.DataFrame(1, columns=["a", "b"], index=range(3))
    print(df1)
    print(df2)
    df3 = pd.concat([df1, df2], axis=0)
    print(df3)


def anliehebing(): # 按列合并
    df1 = pd.DataFrame(0, columns=["a", "b"], index=range(5))
    df2 = pd.DataFrame(1, columns=["a", "b"], index=range(3))
    print(df1)
    print(df2)
    df3 = pd.concat([df1, df2], axis=1)
    print(df3)


def main():
    # anhanghebing() # 按行合并
    anliehebing() # 按列合并


if __name__ == '__main__':
    main()

