import os
import glob
import numpy as np
import operator
from pylab import *
from scipy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
#ax = fig.add_subplot(111, projection= '3d')

colors= raw_input("enter colors")
colors=colors.split()
table= raw_input("enter files")
table=table.split()
names= raw_input("enter names")
names= names.split()
bcg= raw_input("enter BCG")
ageer= raw_input("enter xerr")
ageer= ageer.split()
metaler= raw_input("enter yerr")
metaler= metaler.split()
dir=str("/net/edwards/it66/Summer15/mod_spec/"+bcg)
os.chdir(dir)
x=len(table)
s=[0]*x
area=[0]*x
age=[0]*x
metal=[0]*x
xer=[0]*x
yer=[0]*x
for n in range(0,x):
    fn=table[n]
    f=open(fn)
    lines=f.read().splitlines()
    y=len(lines)
    name=names[n]
    for i in range(0,y):
        line=lines[i]
        columns=line.split()
        a=float(columns[0])
        area[i]=a*20
        b=float(columns[1])
        age[i]=b/10**(9)
        metal[i]=float(columns[2])
    xer[0]=float(ageer[n])/10**9
    xer[1]=float(ageer[n])/10**9
    yer[0]=float(metaler[n])
    yer[1]=float(metaler[n])
    print (xer)
    print (yer)
    xs=age
    print (xs)
    zs=metal
    c1=colors[n]
    m=len(age)
    ys=[n]*m
#    s= ax.scatter(xs, ys, zs, zdir=u'z', s=area, c=c1)
    s= plt.errorbar(xs, zs, xerr=xer, yerr=yer, linestyle= "none", marker="o", c=c1)
'''ax.set_ylim([0,x])
ax.set_zlim([-0.007,0.04])
ax.set_xlim([0,25])
ax.set_xlabel('Age (billions of yrs)')
ax.set_ylabel('Region')
ax.set_zlabel('Metallicity')
ax.set_zticks([-0.007, 0, 0.021, 0.035])
ax.set_xticks([0,5,10,15,20,25])
x=range(0,x)
ax.set_yticks(x)
ax.set_yticklabels(names)
ax.set_title(bcg)'''

plt.ylim([-0.007,0.04])
plt.xlim([0,25])
plt.xlabel('Age (billions of yrs)')
plt.ylabel('Metallicity')
plt.yticks([-0.007, 0, 0.021, 0.035])
plt.xticks([0,5,10,15,20,25])
x=range(0,x)
plt.title(bcg)

plt.savefig(str(bcg+"new.pdf"))
plt.show()
