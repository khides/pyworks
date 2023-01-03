from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data3=pd.read_excel('coil.xlsx',sheet_name='Sheet3')
print(data3)

x3list=[]
y3list1=[]
y3list2=[]

for i in range(len(data3)):
    x3list.append(data3.at[i,'h']*(10**-3))
    y3list1.append(data3.at[i,'Bc'])
    y3list2.append(data3.at[i,'Bm'])

x3=np.linspace(min(x3list),max(x3list),1000)
u0=1.25663726212*(10**-6)
i=1
r=25*(10**-3)
Bci=u0*i*(r**2)/(2*((x3**2+r**2)**(3/2)))*100*1000



#plt.axes().set_aspect('equal')
plt.scatter(x3list,y3list1,label='round coil',s=10)
plt.scatter(x3list,y3list2,label='magnet',s=10)
plt.scatter(x3,Bci,label='ideal data',s=10)
plt.loglog(basex3list=10,basey3list1=10,basey3list2=10,basex3=10,baseBci=10)
plt.xlabel('position (x/mm)')
plt.ylabel('magnetic flux density (B/mT)')
plt.grid()
plt.legend(loc='lower left')
plt.title('measurement of magnetic flux density')
plt.show()



data1=pd.read_excel('coil.xlsx',sheet_name='Sheet1')
print(data1.head)

x1list=[]
y1list=[]


#print(data1.at[1,'Xabs'])
for i in range(len(data1)):
    x1list.append(data1.at[i,'x'])
    y1list.append(data1.at[i,'Bx'])

#plt.plot(x1list,y1list,)
plt.scatter(x1list,y1list,label='original data')
#plt.errorbar(x1list,y1list)
#plt.bar(x1list,y1list,)


x1=np.arange(min(x1list),max(x1list),1)
x1array=np.array(x1list)
y1array=np.array(y1list)

#res1=np.polyfit(x1array,y1array,3)
#poly1=np.poly1d(res1)(x1)

#plt.scatter(x1,poly1,label='Polynomial trendline')
plt.xlabel('coil position (x/mm)')
plt.ylabel('magnetic flux density (Bx/mT)')
plt.grid()
plt.legend()
plt.title('measurement of magnetic flux density of coil (A-D)')
plt.show()


data2=pd.read_excel('coil.xlsx',sheet_name='Sheet2')
print(data2)

x2list=[]
y2list=[]

for i in range(len(data2)):
    x2list.append(data2.at[i,'y'])
    y2list.append(data2.at[i,'By'])

plt.scatter(x2list,y2list)
plt.xlabel('coil position (y/mm)')
plt.ylabel('magnetic flux density (By/mT)')
plt.grid()
plt.legend()
plt.title('measurement of magnetic flux density of coil (F-B)')
plt.show()



