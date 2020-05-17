# -*- coding: utf-8 -*-
"""
Created on Sun May  17 16:00:16 2020
@author: Juxihong Julaiti
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_context("paper")
sns.set_style("darkgrid")

df=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
df['date']=pd.to_datetime(df['date'])
temp=df[df['state']=='Pennsylvania'].sort_values("date")


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
dt,cs=str(temp[temp['county']=='Cumberland'].date.max())[:10],list(temp[temp['county']=='Cumberland'].cases)[-1]
plt.plot(temp[temp['county']=='Cumberland'].date,temp[temp['county']=='Cumberland'].cases,"-x",label="{}: {}".format(dt,cs))
plt.xticks(rotation=45)
plt.legend()
plt.subplot(1,2,2)
plt.plot(temp[temp['county']=='Cumberland'].date,temp[temp['county']=='Cumberland'].cases.shift(-1)-temp[temp['county']=='Cumberland'].cases,"-o")
past_three_day_mean=np.mean(list((temp[temp['county']=='Cumberland'].cases.shift(-1)-temp[temp['county']=='Cumberland'].cases)[-4:])[:-1])
plt.hlines(y=past_three_day_mean,xmin=temp[temp['county']=='Cumberland'].date.min(),xmax=temp[temp['county']=='Cumberland'].date.max(),label="past 3 days mean num. of daily new cases={:.2f}".format(past_three_day_mean),color="blue")
past_seven_day_mean=np.mean(list((temp[temp['county']=='Cumberland'].cases.shift(-1)-temp[temp['county']=='Cumberland'].cases)[-8:])[:-1])
plt.hlines(y=past_seven_day_mean,xmin=temp[temp['county']=='Cumberland'].date.min(),xmax=temp[temp['county']=='Cumberland'].date.max(),label="past 7 days mean num. of daily new cases={:.2f}".format(past_seven_day_mean),color="red")
plt.xticks(rotation=45)
plt.suptitle("Cumberland")
plt.legend()
plt.show()
