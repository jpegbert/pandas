# https://segmentfault.com/q/1010000020503923

import pandas as pd
from numpy import nan as NaN
import numpy as np

data = dict()
data['T1_TeamID'] = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
data['score'] = [50,60,70,60,70,80,70,80,90,60,70,80,70,80,90,80,90,100,90,100,110]
data['score_avg_before'] = [NaN,NaN,NaN,50,60,70,55,65,75,NaN,NaN,NaN,60,70,80,65,75,85,70,80,90]
data['Season'] = ['2018','2018','2018','2018','2018','2018','2018','2018','2018','2019','2019','2019','2019','2019','2019','2019','2019','2019','2019','2019','2019']
data['DayNum'] = [1,1,1,2,2,2,3,3,3,1,1,1,2,2,2,3,3,3,4,4,4]
#create dataframe
test = pd.DataFrame(data)

print(test)

test['score_avg'] = "NaN"
for i in range(0,len(test)):
    if test['DayNum'][i] > 1:
        tmp_sc = test.loc[test.DayNum<test['DayNum'][i]].reset_index(drop=True).groupby(["Season", 'T1_TeamID'])['score'].agg([np.mean]).reset_index()
        test['score_avg'][i] = tmp_sc.loc[(tmp_sc.T1_TeamID==test['T1_TeamID'][i])&(tmp_sc.Season==test['Season'][i])].reset_index(drop=True)['mean'][0]
    else:
        test['score_avg'][i] = "NaN"

print(test)
