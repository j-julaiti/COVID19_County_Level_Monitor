# -*- coding: utf-8 -*-
"""
Created on Sun May  17 16:50:00 2020
@author: Juxihong Julaiti
"""
import json,os, pandas as pd, matplotlib.pyplot as plt, numpy as np
from warnings import filterwarnings
filterwarnings('ignore')

pwd=os.path.dirname(os.path.abspath(__file__))

df=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
df['date']=pd.to_datetime(df['date'])
cty_state_info=pd.read_csv(pwd+"/lib/zip_code_map.csv")
state_abb=json.load(open(pwd+"/lib/us-states-abb.json"))

try:
    config=json.load(open(pwd+"/lib/config.json"))
except:
    zipcode=input("no config is file found, please input the 5-digit ZIP code: ")
    config={}
    config['zip']=int(zipcode)
    
if "County" not in config:
    temp=cty_state_info[cty_state_info['zip code']==config['zip']]
    num_record=temp.shape[0]
    if num_record>=2:
        print("{} records have been found, which county are you looking for?".format(num_record))
        for index,idx in enumerate(temp.index):
            print("    {} {}, {}".format(index+1,temp.loc[idx,'County'],temp.loc[idx,'State']))
        selection=int(input())-1
    else:
        selection=0
    County=list(temp['County'])[selection].replace(" County","")
    State=list(temp['State'])[selection]
    config['State']=State
    config['County']=County
    json.dump(config,open(pwd+"/lib/config.json","w"))
else:
    County=config['County']
    State=config['State']

temp=df[(df['state']==state_abb[State])&(df['county']==County)].sort_values("date").reset_index(drop=False)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
dt,cs=str(temp.date.max())[:10],list(temp.cases)[-1]
plt.plot(temp.date,temp.cases,"-x",label="{}: {}".format(dt,cs))
plt.title("Total Cases")
plt.xticks(rotation=45)
plt.legend()
plt.subplot(1,2,2)
daily_cases=temp.cases-temp.shift(1).cases
plt.plot(temp.date,daily_cases,"-o")
plt.plot(temp.date,daily_cases.rolling(window=7).mean(),color='black',linewidth=1,label='weekly rolling mean')
past_three_day_mean=np.mean(list((temp.cases.shift(-1)-temp.cases)[-4:])[:-1])
plt.hlines(y=past_three_day_mean,xmin=temp.date.min(),xmax=temp.date.max(),label="past 3 days mean num. of daily new cases={:.2f}".format(past_three_day_mean),color="blue")
past_seven_day_mean=np.mean(list((temp.cases.shift(-1)-temp.cases)[-8:])[:-1])
plt.hlines(y=past_seven_day_mean,xmin=temp.date.min(),xmax=temp.date.max(),label="past 7 days mean num. of daily new cases={:.2f}".format(past_seven_day_mean),color="red")
idx_list=list(temp.index)
weekend_start=None
weekend_end=None
for index,idx in enumerate(idx_list[1:]):
    
    dt=temp.loc[idx,'date']
    wkd=dt.weekday()+1
    if not weekend_start and wkd>=6:
        weekend_start=dt
    if wkd==7:
        weekend_end=dt
    if weekend_start!=None and weekend_end!=None:
        plt.axvspan(xmin=weekend_start,xmax=weekend_end,color="green",alpha=0.3)
        weekend_start=None
        weekend_end=None
if wkd>=6 and weekend_start:
    weekend_end=dt
    plt.axvspan(xmin=weekend_start,xmax=weekend_end,color="green",alpha=0.3,label="weekday")
else:
    plt.axvspan(xmin=dt,xmax=dt,color="green",alpha=0.3,label="weekday",ymax=0)
plt.xticks(rotation=45)
plt.title("Daily New Cases")
plt.suptitle("{}, {}, {}".format(County,State,str(temp.date.max())[:-9]))
plt.legend()
plt.show()    
    
