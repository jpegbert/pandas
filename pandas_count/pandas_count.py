import pandas as pd

# https://blog.csdn.net/wendaomudong_l2d4/article/details/83039724

test_data = pd.DataFrame({
    'x1': ["a", "b", "c", "b"],
    "x2": [1, 2, 3, 4],
    "x3": [4, 3, 2, 1]
})
print(test_data)


def count():
    # 统计个数
    print(test_data.x1.count())


def count_nunique():
    # ## 统计不重复的个数
    print(test_data.x1.nunique())


def count_unique():
    ## 得到不重复的值
    ## 返回结果是array
    print(test_data.x1.unique())


def count_freq():
    # 不同于列表，可以直接统计某个值出现的次数，DataFrame需要做一些转换。
    print(list(test_data.x1).count('b'))
    print(sum(test_data.x1.apply(lambda x: 1 if x=='b' else 0)))
    print(test_data.x1.apply(lambda x: 1 if x=='b' else 0).sum())


def groupby_count():
    # 分组统计
    x = pd.DataFrame({
        "x1": ["a", "a", "b", "b", 'c'],
        "x2": [1, 1, 1, 2, 2],
        "x3": [1, 2, 3, 4, 5]
    })
    print(x)
    print(x.groupby(by='x1').count())
    print(x.groupby(by=['x1', 'x2'], as_index=False).count())
    # 这里没有分各个列。
    print(x.groupby(by='x1').size())


def groupby_count_distinct_col1():
    x = pd.DataFrame({
        "x1": ["a", "a", "b", "b", 'c'],
        "x2": [1, 1, 1, 2, 2],
        "x3": [1, 2, 3, 4, 5]
    })
    # 类似于sql：select x1,count(distinct x1),count(distinct x2),count(distinct x3) from table group by x1
    print(x.groupby(by='x1').nunique())


def groupby_count_other():
    #
    x = pd.DataFrame({
        "x1": ["a", "a", "b", "b", 'c'],
        "x2": [1, 1, 1, 2, 2],
        "x3": [1, 2, 3, 4, 5]
    })
    print(x.groupby(by=["x1",'x2']).mean())
    print(x.groupby(by=["x1",'x2']).sum())
    print(x.groupby(by=["x1",'x2'], as_index=False).aggregate(sum))


def groupby_describe():
    x = pd.DataFrame({
        "x1": ["a", "a", "b", "b", 'c'],
        "x2": [1, 1, 1, 2, 2],
        "x3": [1, 2, 3, 4, 5]
    })
    print(x.groupby(by=["x1", 'x2'], as_index=True).describe())
    print(x.groupby(by=["x1", 'x2'], as_index=False).describe())


def main():
    # count() # 统计个数
    # count_nunique() # 统计不重复值个数nunique
    count_unique() # 筛选不重复值
    # count_freq() # 统计某一个值的频数
    # groupby_count() # 分组统计
    # groupby_count_distinct_col1()  # 分组统计
    # groupby_count_other() # x.groupby(by=["x1",'x2']).mean()
    # groupby_describe() # 整体的描述统计


if __name__ == '__main__':
    main()

