s = "123456789"
print(s[-3:])


import numpy as np

tan_x = 250/500/2
tan_y = 190/500/2
x = 0.38231488509280964
y = -0.043185151736417994
height = 1.0798116
yaw = 1.2922013998031616
yaw = yaw*np.pi/180

r = np.array([[x*height*tan_x],
                [y*height*tan_y]]) #機体軸における、目標地点との差(ｍ)
print(r)
rotate = np.array([[np.cos(yaw), -np.sin(yaw)],
                    [np.sin(yaw), np.cos(yaw)]])
r_e = np.dot(rotate,r) #地面固定座標系における、目標地点との差(ｍ)
print(r_e)
print(f"north:{r_e[0]}, east:{r_e[1]}")