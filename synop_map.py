#!/bin/python3

import folium
from matplotlib import colors as mcolors
import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as pp
import numpy as np
import json
import requests
from datetime import datetime
import time
import branca.colormap as cm
import io
import os 
from PIL import Image
#from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#driver.get("http://www.python.org")

#driver.close()

#cd /clusterfs/Documents/weather
    
url='https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1.json'
response=requests.get(url) 
data4=json.loads(response.text)
df4=DataFrame(data4['station'])
df4.columns
#print(df4.name)
print(df4[['latitude','longitude','id','name','height','active']] )

df5=df4[(df4.active==True)]
print(len(df5))
#df6=df5[(df5.id<10000000)]
#print(len(df6))
I=0
for i in df5.id:
#    print(i)

    if I%10==0:
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
                df7=pd.concat([df7,df],axis=0, join='outer')
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
                df7rh=pd.concat([df7rh,df],axis=0, join='outer')
            I+=1
            
            
df8=df5.merge(df7,how='inner',on='id') 
df8=df8.merge(df7rh,how='inner',on='id') 
df8['T'] = df8['T'].astype('float')
df8['rh'] = df8['rh'].astype('float')
df8['longitude'] = df8['longitude'].astype('float')
df8['latitude'] = df8['latitude'].astype('float')

print(df8)

df8.plot.scatter(x = 'longitude', y = 'latitude', c= 'T', s = 10, colormap='hsv_r');
pp.savefig('mapT.png', dpi=100, bbox_inches='tight')
df8.plot.scatter(x = 'longitude', y = 'latitude', c= 'rh', s = 10, colormap='viridis');

pid=os.fork()
if pid==0:
  pp.show()
  
  
print('folium map background')
geo=df8[['latitude','longitude','T']]
dat=df8["date_x"].iloc[0]

m = folium.Map(
    location=[59.5, 17],tiles="Stamen Terrain",
    zoom_start=7, control_scale=True 
)

print('folium map with temperatures')
colormap = cm.LinearColormap(colors=['pink','purple','darkblue','blue','lightblue','cyan','green','lightgreen','yellow','orange','red','brown'], index=range(-40,15,5),vmin=-30,vmax=15)

for index, location_info in geo.iterrows():
    color=colormap(location_info["T"])
    folium.CircleMarker(        
        [location_info["latitude"], location_info["longitude"]],
        radius=10,
        fill=True,
        color=color,
        fill_color=color,
        popup=location_info["T"]
    ).add_to(m)
html = f'''\
<head><title>Temperature map</title></head>\
<center><h2>Temperatur {dat} </h2><br /></center>\
'''

m.get_root().html.add_child(folium.Element(html))
m

print('save folium map ')
img_data = m._to_png(1)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')
pid=os.fork()
if pid==0:
  pp.show()
  
m.save("synop_map.html")


print('folium map rh background')
geo=df8[['latitude','longitude','rh']]
dat=df8["date_x"].iloc[0]

m = folium.Map(
    location=[59.5, 17],tiles="Stamen Terrain",
    zoom_start=7, control_scale=True 
)

print('folium map with rh')
colormap = cm.LinearColormap(colors=['brown','orange','yellow','lightgreen','green','darkgreen'], index=range(50,100,10),vmin=50,vmax=100)

for index, location_info in geo.iterrows():
    color=colormap(location_info["rh"])
    folium.CircleMarker(        
        [location_info["latitude"], location_info["longitude"]],
        radius=10,
        fill=True,
        color=color,
        fill_color=color,
        popup=location_info["rh"]
    ).add_to(m)
html = f'''\
<head><title>Relative humidity map</title></head>\
<center><h2>Relativ fukt {dat} </h2><br /></center>\
'''

m.get_root().html.add_child(folium.Element(html))
m

print('save folium map rh')
img_data = m._to_png(1)
img = Image.open(io.BytesIO(img_data))
img.save('image.png')
pid=os.fork()
if pid==0:
  pp.show()
  
m.save("synop_map_rh.html")


