# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:45:21 2020

@author: Björn Claremar
"""

import math
#import pandas as pd
import numpy as np
from datetime import date
#import matplotlib.pyplot as pp
#import matplotlib.dates as mdates
#import matplotlib.ticker as ticker
#import scipy

def Td_ekvT(T,r,p):
    g=9.82 
    Rd=287.06 
    TK=T+273.15  #Temp i Kelvin
    #print (np.log(abs(TK)))
    E=np.power(10,(24.00978-2957.07/TK-2.20999*np.log(abs(TK))))*r /100  #angtryck i hPa
    Q=.62198*E/(p-.37802*E)  #specifik fuktighet
    TV=(1+.61*Q)*TK  #Virtuell temp i Kelvin
    TD=TK/(1+287.06*TK/0.62198/(2.5008e6-2348.4*T)*np.log(100/r))-273.15  #Daggpunkt i C

    Daggpunkt= np.round(TD, 1)
    specfukt= np.round(Q*10000)/10
    print('Daggpunkt = ' + str(Daggpunkt))
    print('Q = ' + str(specfukt))

    Theta=TK*np.power(1000/p,2/7)-273.15#potentiell temp i C
    cp=1004.71#specifik varmekapacitet
    S=(6*(273.15+TD)-TK)/5#Mattnadspunkt i K
    L=2.5008e6-2348.4*(S-273.15)#Latent varme
    Tae=TK*np.exp(L*Q/cp/S)#Ekvivalenttemperatur i K
    thae=Tae*np.power(1000/p,2/7)-273.15#potentiell ekvivalenttemp i C

    Thae= np.round(thae, 1)
    print('Thae = ' + str(Thae))
    return(Daggpunkt,Thae,specfukt)


#vader=pd.
v1=np.loadtxt('vaderM')
#v1=np(vader)
print(v1)
print(v1[-1,:5])

yy=v1[:,0]
mm=v1[:,1]
dd=v1[:,2]
hh=v1[:,3]
mi=v1[:,4]
l=len(mi)
dat=np.int16(v1[:,:3])
fmt = '%Y.    %m.   %d.'
tt=np.zeros(l)
for i in range(l):
    dt=(str(dat[i,:]))
#    print(dt)
#    print(i)
    tt[i]= (date.toordinal(date(dat[i,0],dat[i,1],dat[i,2])))+hh[i]/24+mi[i]/1440
#    print(tt[i])

T=v1[:,5];
U=v1[:,8];
WD=v1[:,9];
p=v1[:,10];
r=v1[:,11];
Sd=v1[:,12];
[Td,Thae,q]=Td_ekvT(T,r,p)
LFC=np.round(130*(T-Td),0)

for i in range(l):
    print(hh[i],mi[i],T[i],r[i],Td[i],Thae[i],q[i],np.round(p[i]%100),Sd[i],LFC[i])
#  print(hh[-7+i],mi[-7+i],T[-7+i],Td[-7+i],Thae[-7+i],q[-7+i])
#  print(np.transpose(Td),np.transpose(Thae),np.transpose(q))


# prc1h=v1[:,15];
# prc24h=v1[:,17];


#print(v1)
#pp.plot(tt,T)

#days = mdates.DayLocator()   # every year
#hours = mdates.HourLocator()  # every month
#daysFmt = mdates.DateFormatter('%d')
#hoursFmt = mdates.DateFormatter('%h')

#x = np.where(tt >= tt[-1]-1)
#print (x)
#print (tt[x])



