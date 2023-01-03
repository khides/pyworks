import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(font=['Meiryo','Yu Gothic','Hiragino Maru Gothic Pro'])

df=pd.read_excel('coil.xlsx',sheet_name='Sheet1')
print(df.head())

df.plot.scatter(x='x',y='Bx',\
    c='blue',marker='x',s=15,alpha=0.5,label='A-F')
plt.xlabel('コイルの位置　x/m')
plt.ylabel('磁束密度　Bx/mT')
plt.show()