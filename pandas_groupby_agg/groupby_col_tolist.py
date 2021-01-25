import pandas as pd

df = pd.read_csv()
group_data = df.groupby(["col1", "col2"])
data_list = [group_data.get_group(gp)['col3'].tolist() for gp in group_data.groups]

