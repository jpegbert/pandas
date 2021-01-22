import pandas as pd

# https://www.jb51.net/article/166533.htm


df = pd.DataFrame([[1, 2, 2], [1, 4, 5], [1, 2, 4], [1, 6, 3], [2, 3, 1], [2, 4, 1], [2, 3, 5], [3, 1, 1]], columns=['A', 'B', 'C'])
gp = df.groupby(by=['A', 'B'])
print(gp.size())
# gp = df.groupby(by=['A', 'B', 'C'])
newdf = gp.size()
newdf = newdf.reset_index(name='times')
print(newdf)
