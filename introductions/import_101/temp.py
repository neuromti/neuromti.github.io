# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
print('Hello')
printBuffer = 'Hello'
print(printBuffer.upper())

tmpList = []
for i in ('Alpha','House','Door','Window','Garage', 'Garten','Omega'):
    tmpList.append(i)
    
print(tmpList[0])
print(tmpList[-1])
print(tmpList[1:-1])
print(tmpList[-1:1:-1])
##
for id,entry in enumerate(tmpList):
    print(str(id)+ entry)
    
    
tmpDict = {1:'Alpha',2:'Beta',3:'Gamma',4:'Epsilon'}
print(tmpDict)
print(tmpDict[2])

tmpDict.update({'WTF':'Exactly'})
print(tmpDict['WTF'])

print(type(1.0))
print(type(1))

# %%
def printAll(printDict):
    for key,val in printDict.items():
        print('Key: ' ,key, 'Val: ', val)

printAll(tmpDict)
# %%
import numpy as np
import matplotlib.pyplot as plt
# %%

x = np.arange(-100,101,1)
y = x ** 2
z = 10+(x/2)

y = np.power(x,2)

fig, ax = plt.subplots(2, 1)
ax[0].plot(x,y)
ax[0].grid()
ax[1].plot(x,z)
ax[1].grid()
fig.show()
# %%
def myPlotter(ax,x,y,title = 'Line', xlabel='x'):
    ax.plot(x,y)
    ax.grid()
    ax.set_title(title)
    
fig, ax = plt.subplots(1, 2, figsize = (6,3), dpi = 100)
myPlotter(ax[0],x,y,title='Power')
myPlotter(ax[1],x,z)
fig.show()
