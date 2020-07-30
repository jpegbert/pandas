import pandas as pd


df = pd.DataFrame({"sex": list('mmmmmfmf')})
print(df)


def value_count(): # 统计一列各值出现的次数
    tmp_df = df['sex']
    count = tmp_df.value_counts(dropna=False)
    print("==")
    print(count)
    print("==")
    count_dict = dict(count)
    print(count_dict)
    print(type(count_dict))
    rate_dict = {}
    for key, value in count_dict.items():
        rate_dict[key] = value / len(tmp_df)
    print("=============")
    for key, value in rate_dict.items():
        print(key, value)
        if value <= 0.3:
            df.loc[df['sex'] == key, 'sex'] = -1
    print(df)


def main():
    value_count() # 统计一列各值出现的次数


if __name__ == '__main__':
    main()
