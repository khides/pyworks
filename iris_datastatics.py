from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset('iris')
df=pd.DataFrame(data)
print(df.head())


sns.pairplot(data=df,kind='reg',hue='species')
plt.legend()
plt.show(block=False)

input()