import pandas as pd
from matplotlib import pyplot as plt
import japanize_matplotlib
import numpy as np

df_0 = pd.read_excel("/Users/koki_mac/pywork/pyworks/experiment/1a.xlsx", sheet_name="flap0")
df_20 = pd.read_excel("/Users/koki_mac/pywork/pyworks/experiment/1a.xlsx", sheet_name="flap20")

alpha_0 = df_0.iloc[:4, 0]
CL_0 = df_0.iloc[:4, 4]
a_0,b_0 = np.polyfit(alpha_0, CL_0, 1)
print(a_0, b_0)
# print(df_0.columns[0])

alpha_20 = df_20.iloc[:3, 0]
CL_20 = df_20.iloc[:3, 4]
a_20, b_20 = np.polyfit(alpha_20, CL_20, 1)
def poly(alpha, a, b):
    return a*alpha + b

alphalst = np.linspace(-5,15, 1000)
CL0lst = []
CL20lst = []
for alpha in alphalst:
    CL0lst.append(poly(alpha, a_0, b_0))
    CL20lst.append(poly(alpha,a_20, b_20))


fig = plt.figure(figsize=(14,8))
for i in range(4):
    ax = fig.add_subplot(2,3,i+1)
    ax.plot(df_0["α"], df_0[df_0.columns[i+4]], "-o", label = "flap 0°")
    ax.plot(df_20["α"], df_20[df_0.columns[i+4]], "-o", label = "flap 20°")
    # ax.axvline(x=10, color = "r", label = "失速角")
    if i == 0:
        ax.plot(alphalst, CL0lst, c = "gray" , label = f"揚力傾斜 {str(a_0)[:5]}/deg")
        ax.plot(alphalst, CL20lst, c = "gray" , label = f"揚力傾斜 {str(a_20)[:5]}/deg")

    ax.set_xlabel("迎角 α")
    ax.set_ylabel(str(df_0.columns[i+4]))
    ax.grid()
    ax.legend()

ax = fig.add_subplot(2,3,5)
ax.plot(df_0["C_D"], df_0["C_L"], "-o", label = "flap 0°")
ax.plot(df_20["C_D"], df_20["C_L"], "-o", label = "flap 20°")
ax.set_xlabel("C_D")
ax.set_ylabel("C_L")
ax.grid()
ax.legend()

plt.savefig("空力特性グラフ.png")
# plt.show()
