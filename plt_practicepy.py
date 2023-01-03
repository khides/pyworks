import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
ax=fig.add_axes([0,0,0.5,0.5])
plt.show()


plt.subplots(figsize=(15,5))

sizelist=[3,8,100]

for i in range(3):
    size=sizelist[i]
    X,Y=np.meshgrid(np.linspace(0,10,size),np.linspace(0,10,size))
    C=np.linspace(0,100,size*size).reshape(size,size)
    plt.subplot(1,3,i+1)
    plt.pcolormesh(X,Y,C,cmap='rainbow')

plt.show()


array=np.linspace(0,10,101)
import pandas as pd

df=pd.DataFrame(np.linspace(0,100,100*100).reshape(100,100))

import seaborn as sns

sns.heatmap(df,cmap='rainbow')

plt.show(block=False)
input()