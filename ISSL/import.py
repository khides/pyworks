# Q_0 = 86.453
# Q_23 = 79.343
# Wout = [458, 132.5, 701.6, 161.5]

# x = [1.85, 0.54, 2.83, 0.65]
# for i in range(len(x)):
#     T_0 = ((Wout[i]+x[i]*86.453)/(x[i]* 0.8 * 5.67* 10**(-8)))**0.25 - 273.15
#     T_23= ((Wout[i]+x[i]*79.343)/(x[i]* 0.8 * 5.67* 10**(-8)))**0.25 - 273.15

#     print(T_0, T_23)

# # import numpy as np
# # from numpy import linalg as la
# # lst1 = np.array([1,2,3])
# # lst2 = np.array([0,1,2])
# # print(lst1 - lst2)
# # lst1 = np.array([0,3,4])
# # print(la.norm(lst1))

# # lst1 = np.array([[1,2],
# #                  [3,4]])
# # lst2 = np.array([[0,1],
# #                  [2,3]])
# # print(np.dot(lst1,lst2).flatten())












# import numpy as np
# from matplotlib import pyplot as plt

# # パラメタ
# Wpl = 3203.232
# Wf = 2645.919
# dV = 11768.241
# g = 9.8
# Isp1 = 280
# Isp2 = 455
# WA1 = 200
# WA2 = 400

# # 構 造 係 数
# c1 = np.log(300/80)

# def h1(Wp1 ):
#     return 0.07 - 0.01/ c1 * np.log(Wp1 /80)

# c2 = np.log (150/30)

# def h2(Wp2 ):
#     return 0.12 - 0.02/ c2 * np.log(Wp2 /30)

# # 必要ΔVとの差
# def get_V(Wp1, Wp2):
#     W2 = WA2 + (h2(Wp2) + 1)* Wp2 *1000
#     z2 = 975* Wp2 / (Wpl + W2)
#     z1 = 995* Wp1 / (Wpl + W2 + Wf + WA1 + (h1(Wp1) + 1)* Wp1 *1000)
#     return g * Isp1 * np.log(1/(1 - z1)) + g * Isp2 * np.log (1/(1 - z2)) - dV

# # 二分法
# def calc_mean(Wp2):
#     a = 800
#     b = 0
#     while abs (a - b) > 0.001:
#         Wp1 = (a + b)/2
#         if get_V(Wp1 ,Wp2) >0:
#             a = Wp1
#         else :
#             b = Wp1
#     return Wp1

# # 打ち上げ総重
# def totalweight(Wp2):
#     Wp1 = calc_mean(Wp2)
#     W1 = WA1 + (h1(Wp1) + 1)* Wp1 *1000
#     W2 = WA2 + (h2(Wp2) + 1)* Wp2 *1000
#     return (Wpl + Wf + W1 + W2)/1000

# # 可視化
# fig, ax = plt.subplots()
# x1 = np.arange(20 ,100 ,0.01)
# y1 = []
# for i in range(len(x1)):
#     y1.append (totalweight(x1[i]))
# ax.plot (x1,y1)
# ax.set_xlabel("WP2 [t]")
# ax.set_ylabel("W0 [t]")
# ax.grid()
# plt.show()

# # 最小値を求める
# for i in range (0 , len(x1)):
#     if y1[i] == min(y1) :
#         print (f"Wp2 =,{x1[i]},Wp1 =, {calc_mean(x1[i])} , W0=, {y1[i]}")







import numpy as np
from matplotlib import pyplot as plt
Ps = 1358
alpha = 0.2
thetalst = np.linspace(0, 2*np.pi, 1000)
def TAR(beta):
    plus = []
    minus = []
    for theta in thetalst:
        cur = - Ps * alpha * np.cos(beta) * np.cos(theta)
        if cur >0:
            plus.append(cur)
            minus.append(0)
        else :
            plus.append(0)
            minus.append(-cur)
    return plus, minus

def SUN(beta):
    plus = []
    minus = []
    for theta in thetalst:
        cur = - Ps * alpha * np.cos(beta) * np.sin(theta)
        if cur >0:
            plus.append(cur)
            minus.append(0)
        else :
            plus.append(0)
            minus.append(-cur)
    return plus, minus

def PAD(beta):
    plus = []
    minus = []
    for theta in thetalst:
        cur = Ps * alpha * np.sin(beta)
        plus.append(cur)
        minus.append(0)
    return plus, minus


fig = plt.figure()
# plt.xlabel("deg /rad")
for i in range(6):
    ax = fig.add_subplot(2,3,i+1)
    if i == 0:
        ax.plot(thetalst, TAR(0)[0] ,label = "beta = 0")
        ax.plot(thetalst, TAR(23.4*np.pi/180)[0], label = "beta = 23.4")
        ax.set_title("+TAR",loc="left")

    if i == 1:
        ax.plot(thetalst, SUN(0)[0] ,label = "beta = 0")
        ax.plot(thetalst, SUN(23.4*np.pi/180)[0] ,label = "beta = 23.4")
        ax.set_title("+SUN",loc="left")

    if i == 2:    
        ax.plot(thetalst, PAD(0)[0] ,label = "beta = 0")
        ax.plot(thetalst, PAD(23.4*np.pi/180)[0],label = "beta = 23.4")
        ax.set_title("+PAD",loc="left")

    if i == 3:
        ax.plot(thetalst, TAR(0)[1] ,label = "beta = 0")
        ax.plot(thetalst, TAR(23.4*np.pi/180)[1],label = "beta = 23.4")
        ax.set_title("-TAR",loc="left")
    
    if i == 4:
        ax.plot(thetalst, SUN(0)[1] ,label = "beta = 0")
        ax.plot(thetalst, SUN(23.4*np.pi/180)[1],label = "beta = 23.4")
        ax.set_title("-SUN",loc="left")

    if i == 5:
        ax.plot(thetalst, PAD(0)[1] ,label = "beta = 0")
        ax.plot(thetalst, PAD(23.4*np.pi/180)[1],label = "beta = 23.4")
        ax.set_title("-PAD",loc="left")
    
    ax.set_xlabel(("deg /rad"))
    ax.set_ylabel("Q_in")
    ax.legend()
    ax.grid()
    


plt.show()




# while :    
#     time_now = time.time()
#     goal = np.array([latitude_goal,
#                     longitude_goal,
#                     drone.Absolute_altitude_m])
#     current = np.array([drone.Latitude_deg,
#                         drone.Longitude_deg, 
#                         drone.Absolute_altitude_m])
#     dist = la.norm(goal - current)
#     error = 0
#     de = 0
#     ie = 0
#     while dist < 0.5:
#         time_pre = time_now
#         error_pre = error
#         time_now = time.time()
#         T = time_now - time_pre
#         error = goal - current #######

#         ##偏差は本来画像処理のピクセル差で持ってくる################################
#         # height = drone.Lidar
#         # yaw = drone.Yaw_deg
#         # await camera.take_pic()
#         # await camera.detect_center_cv()
        
#         # r = np.array([[camera.x*height*np.tan(alpha)],
#         #               [camera.y*height*np.tan(alpha)]]) #機体軸における、目標地点との差(ｍ)
#         # rotate = np.array([[np.cos(yaw), np.sin(yaw)],
#         #                    -np.sin(yaw), np.cos(yaw)])
#         # r_e = np.dot(r,rotate).flatten() #地面固定座標系における、目標地点との差(ｍ)
        
#         # if la.norm(r_e) < 0.5: #十分近ければ終わり
#         #     break

#         # d_lat = r_e[0]/Cir_md*360 ##緯度差
#         # d_lon = r_e[1]/Cir_eq/np.cos(drone.Latitude_deg)*360 ##経度差
#         # error = np.array([d_lat,
#         #                   d_lon,
#         #                   0])
#         #########################################################################
        
#         if not T == 0: 
#             de = (error - error_pre)/T
#             ie += (error + error_pre)*T/2
#         control = KP*error + KI*ie + KD*de #PID制御による制御量を決定
        
        
#         noise = random.uniform(-1,1) ###########シミュレーション環境ではノイズを意図的に入れる
        
        
#         ##制御器
#         target = control* (1 + noise) + current #実際はnoiseはなし
#         await drone.Loop_goto_location(latitude_target=target[0],
#                                     longitude_target=target[1],
#                                     altitude_target=target[2])
        
#         ##シミュレーション環境でのみ以下の評価をする
#         current = np.array([drone.Latitude_deg,
#                             drone.Longitude_deg, 
#                             drone.Absolute_altitude_m])
#         dist = la.norm(goal - current)