# import serial
# # import csv
# # import os

# # if os.path.exists('serialmonitor.csv') == True:
# #     os.remove('serialmonitor.csv')

# ser=serial.Serial('COM11',19200,timeout=None)

# while True:
#     value = ser.readline().decode('ascii').rstrip(('\n'))
#     # with open('serialmonitor.csv','a') as f:
#     print(value)
    
# # data=ser.read_all()
# # print(data)
# # with open('serialmonitor.csv','a') as f:
# #     print(data,file=f)

# # value  = input("name:")

# # if value:
# #     print(value)

# # data = "aiueo"
# # print(data.index("ue"))


import numpy as np

lst = [1,2,3]
lst = np.array(lst)

lst -= lst[0]
lst *= 10

print(lst)