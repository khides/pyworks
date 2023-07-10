import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

#環境についてのパラメタ
R_0 = 8314.3 # J/(kmolK) 
gam = 1.4
c_p = gam / (gam-1) * R_0 #定圧モル比熱



#燃焼室の諸元
p_c = 10e6 #燃焼室圧力　Pa
MR_c = 4.4 #燃焼室質量混合比(o/f)
# G_co = sp.Symbol("G_co") #燃焼室酸化剤質量流量
# G_cf = sp.Symbol("G_cf") #燃焼室燃料質量流量




#推進剤に関するパラメタ
#酸化剤　F2
W_o = 38# 単位[kg/kmol]　酸化剤剤分子量
rho_o = 1510# 単位[kg/m3]　酸化剤密度

#燃料　H2
W_f = 2# 単位[kg/kmol]　燃料分子量
rho_f = 71# 単位[kg/m3]　燃料密度



#プリバーナの諸元
MR_b = 0#質量混合比(o/f)
# G_bo = sp.Symbol("G_bo")  #ガスジェネレータ酸化剤質量流量
# G_bf = sp.Symbol("G_bf") #ガスジェネレータ燃料質量流量
nR = MR_b*W_f/W_o
M = 1/(1+nR)* W_f + nR/(1+nR)*W_o


#圧力損失
p_1 = sp.Symbol("p_1") #タービン入口圧力
alpha = 0.2
beta = 0.2
gamma = 0.4
dp_ic = alpha*p_c
dp_cool = gamma*p_c
p_po = dp_ic + p_c
p_pf = dp_cool + dp_ic + p_1

#タービン諸元
p_2 = p_c +dp_ic #タービン出口圧力
T_1 = 300 #タービン入口温度
# T_2 = #タービン出口温度
eta_t = 0.75
C_p = gam / (gam-1) * R_0/M #定圧モル比熱

#ポンプ諸元
eta_pdo = 0.7
eta_po = 0.7
eta_pf = 0.7

#質量流量
# G = sp.Symbol("G")
G_cf = 1
G_co = G_cf*MR_c

eq = G_co *p_po/rho_o/eta_po + G_cf*p_pf/rho_f/eta_pf - G_cf*C_p*eta_t*T_1*(1-(p_2/p_1)**((gam-1)/gam))
# fa = sp.solve(eq,p_1)
# print(fa)
pb_lst = np.linspace(1e7, 5e7, 100)
vallst = []
for val in pb_lst:
    vallst.append(eq.subs(p_1,val))

fig,ax = plt.subplots()
ax.plot(pb_lst, vallst)
ax.grid()
plt.show()

# print("p_po:", p_po)
# print("p_pf:", p_pf)