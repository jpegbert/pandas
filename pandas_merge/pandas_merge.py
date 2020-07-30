import pandas as pd

# https://www.cnblogs.com/guxh/p/9451532.html

left = pd.DataFrame({'A': ['a0', 'a1', 'a2', 'a3'],
                         'B': ['b0', 'b1', 'b2', 'b3'],
                         'k1': ['x', 'x', 'y', 'y']})
# right = pd.DataFrame({'C': ['c1', 'c2', 'c3', 'c4'],
#                           'D': ['d1', 'd2', 'd3', 'd4'],
#                           'k1': ['y', 'y', 'z', 'z']})
right = pd.DataFrame({'C': ['c1', 'c2', 'c3', 'c4'],
                          'D': ['d1', 'd2', 'd3', 'd4'],
                          'k1': ['x', 'x', 'x', 'y']})

print("left")
print(left)
print("right")
print(right)


def merge_direct():
    result = pd.merge(left, right)
    # 只有df1和df2的key1=y的行保留了下来，即默认合并后只保留有共同列项并且值相等行（即交集）
    print(result)


def merge_on():
    result = pd.merge(left, right, on='k1')
    # 指定on，设定合并基准列，就可以根据k1进行合并，并且left和right共同列会同时变换名称后保留下来
    print(result)


def merge_how():
    # ‘inner’(默认)：共同列的值必须完全相等：
    result = pd.merge(left, right, on='k1', how='inner')
    print("inner", result)

    # 'outer’：共同列的值都会保留，left或right在共同列上的差集，会对它们的缺失列项的值赋上NaN：
    result = pd.merge(left, right, on='k1', how='outer')
    print("outer", result)

    # ‘left’：根据左边的DataFrame确定共同列的保留值，右边缺失列项的值赋上NaN：
    result = pd.merge(left, right, on='k1', how='left')
    print("left", result)

    # ‘right’：根据右边的DataFrame确定共同列的保留值，左边缺失列项的值赋上NaN：
    result = pd.merge(left, right, on='k1', how='left')
    print("right", result)


def merge_indicator():
    result = pd.merge(left, right, on='k1', how='outer', indicator=True)
    print(result)


def merge_by_muilty_cols():
    left['k2'] = ['1', '2', '3', '4']
    right['k2'] = ['1', '2', '3', '4']
    print("---------------------")
    print("left")
    print(left)
    print("right")
    print(right)
    print("---------------------")
    result = pd.merge(left, right, on=['k1', 'k2'], how='inner')
    # result = pd.merge(left, right, on=['k1', 'k2'], how='left')
    print(result)


def main():
    # merge_direct() # 直接合并
    # merge_on() # 指定on属性
    # merge_how() # 指定how属性
    merge_by_muilty_cols() # 指定多列合并
    # merge_indicator() # 指定indicator属性


if __name__ == '__main__':
    main()
