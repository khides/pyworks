import numpy as np

def outliers_mean(lst):# 四分位範囲から外れ値を除いた平均を求める
    quartile_1, quartile_3 = np.percentile(lst, [25, 75])
    iqr = quartile_3 - quartile_1
    # 下限
    lower_bound = quartile_1 - (iqr * 1.5)
    # 上限
    upper_bound = quartile_3 + (iqr * 1.5)
    array = np.array(lst)[((lst < upper_bound) & (lst > lower_bound))]
    mean = np.average(array)
    return mean, array

x = [1,5,5,5,6,6,6,7,7,8,8,10]

print(outliers_mean(x))