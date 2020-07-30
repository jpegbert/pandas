import pandas as pd

# 先创建一个数据框（包含缺失值）
df = pd.DataFrame({'auth': ['spring', 'summer', 'fall', 'spring'],
                   'sply': ['a', 'c', 'a', 'b'],
                   'name': ['zhangsan', 'lisi', 'xiaohua', 'xiaomei']})

# categorical_name = ['auth', 'sply', 'name']
categorical_name = ['name']

print(df)

# 定义一个循环函数，处理分类型特征，进行标签编码
def categorical_preprocessing(dataset, categorical_feature):
    '''
    param:
        dataset:DataFrame,输入的数据集
        categorical_feature:list,分类特征列名
    '''
    for feature in categorical_feature:
        set_feature = set(dataset[feature])  # 将特征映射到集合中
        dic_feature = {}
        for i, feat in enumerate(set_feature):
            dic_feature[feat] = i
            # print("feat:", feat, "index:", i)
        # dataset[feature] = dataset[feature].map(dic_feature)
        dataset[feature] = dataset.set_index([feature]).index.map(dic_feature.get)
    # dataset = pd.get_dummies(dataset, columns=categorical_feature)
    return dataset


# 处理分类特征编码
dataset = categorical_preprocessing(df, categorical_name)

print(dataset)
print("====")
print(dataset["name"].unique().tolist())

