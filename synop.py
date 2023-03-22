import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as pp
import numpy as np
import json
import requests
from datetime import datetime
import time
import cartopy.crs as crs
from cartopy.feature import NaturalEarthFeature
import cartopy.feature as cfeature
import cartopy
import folium
from matplotlib import colors as mcolors

url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/97510/period/latest-hour/data.json' 
response=requests.get(url) 
data=json.loads(response.text)
df=DataFrame(data['value'])
_=df.rename(columns={'value':'T'},inplace=True)
df['date'] = pd.to_datetime(df['date']/1000,unit='s')  
#print(df)
url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/6/station/97510/period/latest-hour/data.json' 
response=requests.get(url) 
data2=json.loads(response.text)
df2=DataFrame(data2['value'])
_=df2.rename(columns={'value':'rh'},inplace=True)
_=df2.rename(columns={'quality':'qu2'},inplace=True)
df2['date'] = pd.to_datetime(df2['date']/1000,unit='s')
#print(df2)
#pd.concat(df,df2,left_on='date',right_index=True)
df3=df.merge(df2,how='inner',on='date')
#pd.concat(df,df2)
print(df3)

#exit()
url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1.json'
response=requests.get(url) 
data4=json.loads(response.text)
df4=DataFrame(data4['station'])
df4.columns
df4.height.plot()
#print(df4.name)
print(df4[['latitude','longitude','id','name','height','active']] )

df5=df4[(df4.active==True)]
print(len(df5))
#df6=df5[(df5.id<10000000)]
#print(len(df6))
I=0
for i in df5.id:
#    print(i)

    print(I)
    url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/'+str(i)+'/period/latest-hour/data.json'
    url2='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/6/station/'+str(i)+'/period/latest-hour/data.json'
    response=requests.get(url)
    if response.status_code == 200:
        data=json.loads(response.text)
        df=DataFrame(data['value'])
        if df.empty == 0:
            _=df.rename(columns={'value':'T'},inplace=True)
            df['date'] = pd.to_datetime(df['date']/1000,unit='s') 
            df['id'] = i 
            if I==0:
                df7=df
            else:
                df7=df7.append([df])
    response=requests.get(url2)
    if response.status_code == 200:
        data=json.loads(response.text)
        df=DataFrame(data['value'])
        if df.empty == 0:
            _=df.rename(columns={'value':'rh'},inplace=True)
            df['date'] = pd.to_datetime(df['date']/1000,unit='s') 
            df['id'] = i 
            if I==0:
                df7rh=df
            else:
                df7rh=df7rh.append([df])
            I+=1


    #_=df.rename(columns={'value':'T'},inplace=True)
print(I)    
print(df7) 
df8=df5.merge(df7,how='inner',on='id') 
df8=df8.merge(df7rh,how='inner',on='id') 
df8['T'] = df8['T'].astype('float')
df8['rh'] = df8['rh'].astype('float')
print(df8)
df8.plot.scatter(x = 'longitude', y = 'latitude', c= 'T', s = 10, colormap='hsv_r');


df8.plot.scatter(x = 'longitude', y = 'latitude', c= 'rh', s = 10, colormap='viridis');

#m = folium.Map(location=[bike_station_locations.Latitude.mean(), bike_station_locations.Longitude.mean()], zoom_start=14, control_scale=True
m = folium.Map(
    location=[df8.latitude.mean(), df8.longitude.mean()],
    zoom_start=5, control_scale=True 
)
#for lat, lon, T in df8[['latitude','longitude','T']]:
#    folium.CircleMarker(        
#        location=[lat, lon],
#        radius=10,
#        fill=True,
#        fill_color=T,
#        color=T,
#    ).add_to(m)
m
#pp.scatter(df8.longitude,df8.latitude,c=(df8.T),s=10)

pp.show()

