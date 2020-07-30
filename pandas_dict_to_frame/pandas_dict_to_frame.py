import pandas as pd

data = {'m': 6, 'f': 2}
ind = [i for i in range(len(data))]
print(ind)
df = pd.DataFrame(data, index=ind)
print(df)
