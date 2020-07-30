import pandas as pd

# https://www.cnblogs.com/zongfa/p/9305657.html


df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])

df.columns = ['color', 'size', 'prize', 'class label']

size_mapping = {
    'XL': 3,
    'L': 2,
    'M': 1}
df['size'] = df['size'].map(size_mapping)

class_mapping = {label: idx for idx, label in enumerate(set(df['class label']))}
df['class label'] = df['class label'].map(class_mapping)

df['newcol'] = df["color"] + df["size"].map(str)
# df['newcol'] = df["color"].str.cat(df["size"].map(str))

print(df.columns)
print(df)