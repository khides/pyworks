import logger
from logger import logger_info, log_file_r,log_format
import time

logger_info.info("Hello World")
logger_info.info(log_format('Hold',100,35,135))
time.sleep(2)
logger_info.info(log_format('Hold',100,35,135))
time.sleep(2)
logger_info.info(log_format('Hold',100,35,135))
time.sleep(2)
logger_info.info(log_format('Hold',100,35,135))


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from logger import logger_info, log_file_r

str(datetime.today()) + '_logger'

df = pd.read_csv('.\log'+ log_file_r)


print(df.iloc[2]["Distance"])
fig, ax = plt.subplots()
while True:
    try:
        x = []
        y = []

        df = pd.read_csv('.\log'+ log_file_r)
        for i in range(len(df)):
            if df.iloc[i]["Message"] == 'Hold':
                x.append(datetime.strptime(str(df.iloc[i]['Timeinfo'])[:19], '%Y-%m-%d %H:%M:%S'))
                y.append(df.iloc[i]["Distance"])

        suptime = x[-1]
        inftime = suptime - timedelta(minutes=1)
        suptime = suptime + timedelta(seconds= 5)    
        ax.set_xlim(inftime, suptime)
        print(x)
        plot = ax.plot(x,y)
        plt.pause(0.001)
        # plt.show()
        # plt.savefig('./log'+ log_file_r [:22] + 'lidar.pdf')
        
    except KeyboardInterrupt:
        break
        # x = []
        # y = []

        # df = pd.read_csv('.\log'+ log_file_r)
        # for i in range(len(df)):
        #     if df.iloc[i]["Message"] == 'Hold':
        #         x.append(datetime.strptime(str(df.iloc[i]['Timeinfo'])[:19], '%Y-%m-%d %H:%M:%S'))
        #         y.append(df.iloc[i]["Distance"])

        # suptime = x[-1]
        # inftime = suptime - timedelta(minutes=1)
        # suptime = suptime + timedelta(seconds= 5)    
        # ax.set_xlim(inftime, suptime)
        # print(x)
        # plot = ax.plot(x,y)
        # plt.savefig('./log'+ log_file_r [:22] + 'lidar.pdf')
        
plt.savefig('./log'+ log_file_r [:22] + 'lidar.pdf')