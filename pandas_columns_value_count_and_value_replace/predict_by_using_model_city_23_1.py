import pandas as pd


df = pd.DataFrame({"id": [25, 53, 15, 47, 52, 54, 45, 9],
                   "sex": list('mmmmmfmf'),
                   'score': [1.2, 2.3, 3.4, 4.5, 6.4, 5.7, 5.6, 4.3],
                   "name": ['daisy', 'tony', 'peter', 'tommy', 'ana', 'david', 'ken', 'jim']})
print(df)


def method1(): # 方法1
    df.loc[df['sex'] == 'f', 'sex'] = 0
    df.loc[df['sex'] == 'm', 'sex'] = 1
    print(df)


def method2(): # 方法2
    df.sex[df['sex'] == 'm'] = 1
    df.sex[df['sex'] == 'f'] = 0
    print(df)


def value_count(): # 统计一列各值出现的次数
    tmpa = df['sex']
    a = tmpa.value_counts(dropna=False)
    count_dict = dict(a)
    print(count_dict)
    print(type(count_dict))
    rate_dict = {}
    for key, value in count_dict.items():
        rate_dict[key] = value / len(tmpa)
    print("=============")
    for key, value in rate_dict.items():
        print(key, value)
        if value <= 0.3:
            df.loc[df['sex'] == key, 'sex'] = -1
    print(df)


def main():
    # method1() # 方法1
    # method2() # 方法2
    value_count() # 统计一列各值出现的次数


if __name__ == '__main__':
    main()

