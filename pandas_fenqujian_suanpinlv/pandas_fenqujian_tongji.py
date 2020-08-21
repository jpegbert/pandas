import pandas as pd

# https://blog.csdn.net/weixin_37665577/article/details/106768190?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduend~default-2-106768190.nonecase&utm_term=pandas%E7%BB%9F%E8%AE%A1%E5%9C%A8%E6%9F%90%E4%B8%AA%E5%8C%BA%E9%97%B4%E7%9A%84%E6%95%B0%E5%80%BC%E4%B8%AA%E6%95%B0

df = pd.read_csv("")
# 先按固定的区间分箱，我没用qcut，用的cut不知道什么区别，但是都能用
a = pd.cut(df['Times'], [0, 2000, 3000, 4000, 5000, 10000, 50000], labels=[2000, 3000, 4000, 5000, 10000, 50000])
a = pd.Series(a, name='Times')
# groupby提取汇总统计值
results = pd.Series(df['Times']).groupby(a).agg(['count']).reset_index()
