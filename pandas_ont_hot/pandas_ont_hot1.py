import pandas as pd

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'prize', 'class label']
df2 = pd.get_dummies(df['size'])
print(df2)
print(df2.columns)
# print(type(df2.columns))
# print(df2.columns[0])
cols = [col for col in df2.columns]
# print(len(df2.columns))
print("cols:", cols)
print("df2.columns[0]:", df2.columns[0])
df['newcol'] = df2[df2.columns[0]].map(str)
print("df['newcol']:", df['newcol'])
for index, col in enumerate(df2.columns[1:]):
    # print(index, col)
    df['newcol'] = df['newcol'] + df2[col].map(str)
print(df.columns)
# df.drop(['size', 'prize'], axis=1, inplace=True)
print(df)
