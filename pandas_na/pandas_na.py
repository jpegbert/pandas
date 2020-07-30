import pandas as pd
import numpy as np


df = pd.DataFrame({'value':[np.nan, np.nan, 1, 5, 7]})
print (df)
# count = df['value'].isna().sum() #或者 count = df['value'].isnull().sum()
count = df['value'].isnull().sum()
print (count)

pd.read_csv()



