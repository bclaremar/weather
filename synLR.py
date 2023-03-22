import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
import json
import requests
from datetime import datetime

url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/97510/period/latest-day/data.json' 
response=requests.get(url) 
data=json.loads(response.text)
df=DataFrame(data['value'])
_=df.rename(columns={'value':'T'},inplace=True)
df['date'] = pd.to_datetime(df['date']/1000,unit='s')  
#print(df)
url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/6/station/97510/period/latest-day/data.json' 
response=requests.get(url) 
data2=json.loads(response.text)
df2=DataFrame(data2['value'])
_=df2.rename(columns={'value':'rh'},inplace=True)
_=df2.rename(columns={'quality':'qu2'},inplace=True)
df2['date'] = pd.to_datetime(df2['date']/1000,unit='s')
#print(df2)
#pd.concat(df,df2,left_on='date',right_index=True)
df3=df.combine_first(df2)
#pd.concat(df,df2)
print(df3)

url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1.json'
response=requests.get(url) 
data4=json.loads(response.text)
df4=DataFrame(data4['station'])

print(df4[['latitude','longitude','id','name','height']] ) 
print(df4.loc[df4['id'] == 97510])
print(df4[['latitude','longitude','id','name','height']][790:791] ) 
formH="%20.5f%20.5f%-40s%-40s%-40s%-40s%20.5f%10i%10i%10i%10i%10i%-10s%-10s%-10s%10i%10i%-20s%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i\n"
formD="%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i%13.5f%7i\n"
formE=formD
formT="%7i%7i%7i\n"
id='97510'
FM='FM‑12'
src="SMHI"
h=pd.to_numeric(df4['height'][790:791])
slp=-888888.00000 
slpQ=0
p0=-888888.00000 
p0Q=0
TM=-888888.00000
TMQ=0
SST=-888888.00000
SSTQ=0
PSFC=-888888.00000
PSFCQ=0
pr=-888888.00000
prQ=0
Tx=-888888.00000
TxQ=0
Tn=-888888.00000
TnQ=0
Tnn=-888888.00000
TnnQ=0
P3t=-888888.00000
P3tQ=0
P24t=-888888.00000
P24tQ=0
CC=-888888.00000
CCQ=0
ceil=-888888.00000
ceilQ=0
PW=-888888.00000
PWQ=0

P=100000
PQ=0
H=-888888.00000
HQ=0
T2=273.13
T2Q=0
TD=-888888.00000
TDQ=0
WS=-888888.00000
WSQ=0
WD=-888888.00000
WDQ=0
U=-888888.00000
UQ=0
V=-888888.00000
VQ=0
RH=90
RHQ=0
THN=-888888.00000
THNQ=0
#slp,slpQ,p0,p0Q,TM,TMQ,SST,SSTQ,PSFC,PSFCQ,pr,prQ,Tx,TxQ,Tn,TxQ,Tnn,TnnQ,P3t,P3tQ,P24t,P24tQ,CC,CCQ,ceil,ceilQ,PW,PWQ
#P,PQ,H,HQ,T2,T2Q,TD,TDQ,WS,WSQ,WD,WDQ,U,UQ,V,VQ,RH,RHQ,THN,THNQ
print (h)
date='20221206120000'
print(formH % (59.8471,17.632,id,'Uppsala Aut',FM,src,h,0,0,0,0,0,'F','T','F',0,0,date,slp,slpQ,p0,p0Q,TM,TMQ,SST,SSTQ,PSFC,PSFCQ,pr,prQ,Tx,TxQ,Tn,TxQ,Tnn,TnnQ,P3t,P3tQ,P24t,P24tQ,CC,CCQ,ceil,ceilQ,PW,PWQ
))
print(formD % (P,PQ,H,HQ,T2,T2Q,TD,TDQ,WS,WSQ,WD,WDQ,U,UQ,V,VQ,RH,RHQ,THN,THNQ))
print(formE % (-777777.00000,0,-777777.00000,0,T2,T2Q,TD,TDQ,WS,WSQ,WD,WDQ,U,UQ,V,VQ,RH,RHQ,THN,THNQ))
print(formT % (1,0,0))

import sys
f = open("/clusterfs2/WRF/OBSGRID/obs:"+str(date)[0:10],'w')
f.write(formH % (59.8471,17.632,id,'Uppsala Aut',FM,src,h,0,0,0,0,0,'F','T','F',0,0,date,slp,slpQ,p0,p0Q,TM,TMQ,SST,SSTQ,PSFC,PSFCQ,pr,prQ,Tx,TxQ,Tn,TxQ,Tnn,TnnQ,P3t,P3tQ,P24t,P24tQ,CC,CCQ,ceil,ceilQ,PW,PWQ
))
f.close()
f = open("/clusterfs2/WRF/OBSGRID/obs:"+str(date)[0:10],'a')
f.write(formD % (P,PQ,H,HQ,T2,T2Q,TD,TDQ,WS,WSQ,WD,WDQ,U,UQ,V,VQ,RH,RHQ,THN,THNQ))
f.write(formE % (-777777.00000,0,-777777.00000,0,T2,T2Q,TD,TDQ,WS,WSQ,WD,WDQ,U,UQ,V,VQ,RH,RHQ,THN,THNQ))
f.write(formT % (1,0,0))
f.close()
