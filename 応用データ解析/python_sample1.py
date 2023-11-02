import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.array([12, 16, 16, 16, 24, 24, 28, 32, 52, 80])

mean = np.mean(data)
# mean = data.mean()
print(f'mean = {mean:.2f}')

var = np.var(data)
# var = data.var()
print(f'var = {var:.2f}')

std = np.std(data)
# std = data.std()
print(f'std = {std:.2f}')

skew = stats.skew(data)
print(f'skew = {skew:.2f}')

kurtosis = stats.kurtosis(data)
print(f'kurtosis = {kurtosis:.2f}')

plt.hist(data, bins=100)
plt.show()

##  csvファイルを読み込む場合
csv_data = np.loadtxt('syotoku.csv', delimiter=",").T
plt.plot(csv_data[0], csv_data[1])


## 相関係数
xa = np.array( [75, 87, 86, 82, 81, 83, 89, 84, 86, 85, 83, 70, 72, 93, 78, 65, 84, 85, 66, 84, 80, 78, 75, 71, 82, 74, 84, 77, 79, 76, 83, 75, 86, 76, 80, 76, 68, 72, 75, 85])
xb = np.array( [64, 77, 79, 73, 89, 82, 59, 87, 80, 75, 65, 79, 63, 74, 74, 72, 69, 83, 90, 73, 88, 59, 62, 80, 64, 74, 81, 70, 69, 67, 81, 67, 72, 71, 72, 78, 78, 82, 72, 71])

np_cor = np.corrcoef(xa,xb)
print(np_cor)

