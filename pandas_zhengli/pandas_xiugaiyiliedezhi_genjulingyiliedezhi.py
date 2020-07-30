import pandas as pd


df = pd.DataFrame({"sex": list('mmff'),
                   'score': [1.2, 2.3, 3.4, 4.5]})
print(df)


def method1(): # 方法1
    df.loc[df['sex'] == 'f', 'sex'] = 0
    df.loc[df['sex'] == 'm', 'sex'] = 1
    # df.loc[df['sex'] == 'f', 'score'] = 0
    # df.loc[df['sex'] == 'm', 'score'] = 1
    print(df)


def method2(): # 方法2
    df.sex[df['sex'] == 'm'] = 1
    df.sex[df['sex'] == 'f'] = 0
    # df.score[df['sex'] == 'f'] = 0
    # df.score[df['sex'] == 'm'] = 1
    print(df)


def main():
    # method1() # 方法1
    method2() # 方法2


if __name__ == '__main__':
    main()

