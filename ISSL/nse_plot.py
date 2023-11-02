from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 

# df = pd.read_csv('/Users/koki_mac/pywork/pyworks/ISSL/nse.csv')
df = pd.read_csv('/Users/koki_mac/pywork/pyworks/ISSL/arliss.csv')
altlst = []
latlst = []
lonlst = []

for i in range(len(df)):
    if df.iloc[i]["Message"] == "HOLD":
        if df.iloc[i]["Relative Altitude"] < -11 :
            break
        altlst.append(df.iloc[i]["Relative Altitude"])
        # altlst.append(df.iloc[i]["Distance"])
        latlst.append(df.iloc[i]["Latitude"])
        lonlst.append(df.iloc[i]["Longitude"])
        
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot(latlst, lonlst, altlst)
ax.scatter(latlst[0], lonlst[0], altlst[0], color = "g", label = "start")
ax.scatter(latlst[-1], lonlst[-1], altlst[-1], color = "r", label = "goal")

ax.set_xticks(np.arange(40.850,40.900, 0.01) )
ax.set_yticks(np.arange( -119.1110, -119.1094, 0.0004))
# # ax.set_xticks(np.arange(40.850,40.900, 0.01) )
# ax.set_yticks(np.arange( 139.98752, 139.98768, 0.00004))

ax.set_xlabel("latitude (°)",  labelpad = 10, loc = "right")
ax.set_ylabel("longitude (°)", labelpad = 10, loc = "top")
ax.set_zlabel("altitude from ground (m)", labelpad = 5)
plt.legend()
plt.show()