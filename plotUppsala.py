#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:45:21 2020
#
#@author: Björn Claremar
"""

import math
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as pp
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import scipy

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
    return(TD,Thae,specfukt)


#vader=pd.
v1=np.loadtxt('vaderU')
#v1=np(vader)
#print(v1)
#print(v1[-1,:5])

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
    tt[i]= (date.toordinal(date(dat[i,0]-1969,dat[i,1],dat[i,2])))-1+hh[i]/24+mi[i]/1440
#    print(tt[i])

T=v1[:,5];
U=v1[:,8];
WD=v1[:,9];
p=v1[:,10];
r=v1[:,11];
print(r)
Sd=v1[:,12];
[Td,Thae,q]=Td_ekvT(T,r,p)

# prc1h=v1[:,15];
# prc24h=v1[:,17];
prh=v1[:,14];
pr=prh*0;
for i in range(l):
    if i==0 or prh[i]==0:
        pr[i]=prh[i]
    elif i>0 and i<6:
        pr[i]=prh[i]-prh[i-1]
    elif i>=6:
        pr[i]=prh[i]-prh[i-1]+pr[i-6]
    pr[i]=np.round(100*pr[i])/100


#print(v1)
#pp.plot(tt,T)

days = mdates.DayLocator()   # every year
hours = mdates.HourLocator()  # every month
daysFmt = mdates.DateFormatter('%d')
hoursFmt = mdates.DateFormatter('%h')

x = np.where(tt >= tt[-1]-1)
#print (x)
#print (tt[x])

#for jj in range(1):
j=1
#pp.figure(j)
#fig=plt.figure(1,figsize=(6,12))
fig,axs=pp.subplots(7,1,figsize=(5,12))

#pp.rcParams.update({'figure.figsize': (6,12})
for nn, ax in enumerate(axs):
    if nn==0:
        ax.plot(tt[x],Td[x])
        ax.plot(tt[x],T[x])
        ax.plot(tt[x],Thae[x])
        ax.plot(tt[x],Thae[x]*0,color='black')
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylabel("Temp")
        ax.yaxis.set_major_locator(ticker.MaxNLocator(3))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    elif nn==1:
        ax.plot(tt[x],r[x])
       # ax.plot(tt[x],r[x]*0,color='black')
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylabel("RH")
        #ax.set_ylim(30,100)
        ax.set_yticks(range(40,101,10))
#        ax.yaxis.set_major_locator(ticker.MaxNLocator(3))
#        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    elif nn==2:
        ax.plot(tt[x],U[x])
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylabel("WS")
        ax.set_ylim(0,10)
        ax.set_yticks(range(0,11,2))
#        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    elif nn==3:
        ax.scatter(tt,WD)
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylim(0,360)
        ax.set_yticks(range(0,361,90))
        ax.set_ylabel("WD")
    elif nn==4:
        ax.plot(tt[x],Sd[x], label='SW') 
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylim(0,400)
        ax.set_yticks(range(0,401,100))
        ax.set_ylabel("Rad")
    elif nn==5:
        ax.plot(tt[x],(T[x]-Td[x])*130)
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        #ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_ylim(0,1500)
        ax.set_yticks(range(0,1501,300))
#        ax.set_yticks(range(0,361,90))
        ax.set_ylabel("LCL")
    elif nn==6:
        ax.plot(tt[x],np.sqrt(prh[x]))
#        xAxis = [i + 0.5 for i, _ in enumerate(tt(x))]
        ax.bar(tt[x],np.sqrt(pr[x]),width=1/144)
        if j==1:
            ax.set_xlim(tt[-1]-1,tt[-1])
        ax.set_xlim(tt[-1]-1,tt[-1])
 #       ax.set_ylim(0,5)
 #       ax.set_yticks(range(0,6,1))
        yticks=[0, .1, .2, .5,  1., 2., 5., 10.000]
        ax.set_yticks(np.sqrt(yticks))
        ax.set_yticklabels(yticks)
        ax.set_ylabel("precip (mm/10m)")
    ax.grid(True)
           
    locator = mdates.AutoDateLocator(minticks=3, maxticks=13)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
axs[0].set_title('Uppsala')
pp.savefig('figU.png', dpi=100, bbox_inches='tight')
pp.show()
# format the ticks
# ax.xaxis.set_major_locator(days)
# ax.xaxis.set_major_formatter(daysFmt)
# ax.xaxis.set_minor_locator(hours)
# ax.xaxis.set_major_locator(hours)
# ax.xaxis.set_major_formatter(hoursFmt)


