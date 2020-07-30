import pandas as pd

# https://www.cnblogs.com/bravesunforever/p/11219299.html
# https://blog.csdn.net/jingjing_94/article/details/89195791
# pandas 时间字符串转换得到年月日的两种方法

df = pd.DataFrame(['2019-12-09', '2019-12-02'], columns=["date"])


def date_str_to_datetime():
    # 转换成时间类型
    df["date"] = pd.to_datetime(df["date"], format='%Y-%m-%d')
    df["year"] = pd.to_datetime(df["date"]).dt.year
    df["month"] = pd.to_datetime(df["date"]).dt.month
    df["day"] = pd.to_datetime(df["date"]).dt.day
    df["week"] = pd.to_datetime(df["date"]).dt.week
    print(df)
    print(df.dtypes)


def date_str_to_datetime2():
    # 转换为时间
    df["date"] = pd.to_datetime(df["date"])
    # 获取年月日
    df["year-month-day"] = df["date"].apply(lambda x: x.strftime("%Y-%m-%d"))
    # 获取年
    df["year"] = df["date"].apply(lambda x: x.strftime("%Y"))
    # 获取月
    df["month"] = df["date"].apply(lambda x: x.strftime("%m"))
    # 获取日
    df["day"] = df["date"].apply(lambda x: x.strftime("%d"))
    # 获取月日
    df["month-day"] = df["date"].apply(lambda x: x.strftime("%Y-%m"))
    # 获取周
    df['week'] = df['date'].apply(lambda x: x.strftime('%W'))
    print(df)
    print(df.dtypes)


def main():
    # date_str_to_datetime() # 方法一
    date_str_to_datetime2() # 方法二


if __name__ == '__main__':
    main()
