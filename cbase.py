#!/bin/python3
# coding: utf-8
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from numpy import genfromtxt
from datetime import date
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


C= genfromtxt('cb', delimiter='')
print(C)
yy=2022
mm=(C[:,0])
dd=(C[:,1])
hh=(C[:,2])
mi=(C[:,3])
#mm=mm.where(dd>29, mm-1)
print(mm)
l=len(mi)
#dat=np.int16(v1[:,:3])
tt=np.zeros(l)
for i in range(l):
    tt[i]= (date.toordinal(date(2022-1969,int(mm[i]),int(dd[i]))))-1+(1+hh[i])/24+mi[i]/1440

fig=plt.figure(0,figsize=(5,5))
ax=fig.add_subplot(1,1,1)
#ax.plot(my_data[:,-4:])
#plt.show()
f=30.5
ax.plot(tt,np.sqrt(C[:,-5]*f),'_',label='VV')
ax.plot(tt,np.sqrt(C[:,-4]*f),'2',label='FEW')
ax.plot(tt,np.sqrt(C[:,-3]*f),'p',label='SCT')
ax.plot(tt,np.sqrt(C[:,-2]*f),'d',label='BKN')
ax.plot(tt,np.sqrt(C[:,-1]*f),'s',label='OVC')
ax.legend(loc='best')
locator = mdates.AutoDateLocator(minticks=3, maxticks=13)
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_xlim(min(tt),max(tt))
ax.set_ylim(0,90)
yticks=[50, 100, 200, 300, 500, 700, 1000, 1500, 2000, 3000, 4000, 5000, 7000, 8000]
ax.set_yticks(np.sqrt(yticks))
ax.set_yticklabels(yticks)
ax.grid(True)
plt.savefig('cbase.png', dpi=100, bbox_inches='tight')

fig=plt.figure(1)
ax=fig.add_subplot(1,1,1)
#ax.plot(my_data[:,-4:])
#plt.show()
f=30.5
ax.plot(tt,C[:,-5]*f,'1',label='VV')
ax.plot(tt,C[:,-4]*f,'2',label='FEW')
ax.plot(tt,C[:,-3]*f,'p',label='SCT')
ax.plot(tt,C[:,-2]*f,'d',label='BKN')
ax.plot(tt,C[:,-1]*f,'s',label='OVC')
ax.legend(loc='best')
locator = mdates.AutoDateLocator(minticks=3, maxticks=13)
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_xlim(min(tt),max(tt))
ax.set_ylim(0,1600)
ax.grid(True)
plt.savefig('cbase2.png', dpi=100, bbox_inches='tight')


plt.show()
