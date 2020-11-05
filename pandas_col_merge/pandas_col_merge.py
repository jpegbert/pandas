import pandas as pd


df = pd.DataFrame({'A': [3, 4, 8, 9], 'B': [1.2, 2.4, 4.5, 7.3], 'C': ["aa", "bb", "cc", "dd"]})
df['col'] = df['A'].map(str) + "/" + df['B'].map(str) + "/" + df['C'].map(str)
print(df.head(5))
