import pandas as pd


# https://www.cnblogs.com/TTyb/p/9717554.html

df = pd.DataFrame({'id_part': ["d", "b", "c", "d", "d"],
                   'pred': [0.122817, 0.015449, 0.019208, 0.050064, 0.123],
                   'pred_class': ["woman", "other", "cat", "dog", "dog"],
                   "v_id": ["d1", "d2", "d3", "d1", "d1"]
                   })
print(df)

df1 = df.groupby(['v_id', 'id_part'])['pred_class'].apply(lambda x: list(set(list(x)))).reset_index()
print(df1)

# df2 = df.groupby(['v_id']).agg({'pred_class': [', '.join], 'pred': lambda x: list(x), 'id_part': 'first'}).reset_index()
# print(df2)
