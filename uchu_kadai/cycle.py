import numpy as np
import sympy as sp


#燃焼室の諸元
p_c = 10e6 #燃焼室圧力　Pa
MR_c = 4.4 #燃焼室質量混合比(o/f)
G_co = ########## #燃焼室酸化剤質量流量
G_cf = ########## #燃焼室燃料質量流量




#推進剤に関するパラメタ
#酸化剤　F2
W_o = 38# 単位[kg/kmol]　酸化剤剤分子量
rho_o = 1510# 単位[kg/m3]　酸化剤密度

#燃料　H2
W_f = 2# 単位[kg/kmol]　燃料分子量
rho_f = 71# 単位[kg/m3]　燃料密度



#ガスジェネレータの諸元
MR_g = 0.9 #ガスジェネレータ質量混合比(o/f)
G_go = ########### #ガスジェネレータ酸化剤質量流量
G_gf = ###########ガスジェネレータ燃料質量流量
p_g = ############


#圧力損失
alpha = 0.2
beta = 0.2
gamma = 0.4
dp_ic = alpha*p_c
dp_ig = p_g
dp_cool = gamma*p_c


#タービン諸元
p_1 = p_g #タービン入口圧力
p_2 = 1013e2 #タービン出口圧力
T_1 = 780 #タービン入口温度
# T_2 = #タービン出口温度
eta_t = 0.5

#ポンプ諸元
p_po = dp_ig + p_g
p_pf = dp_ic + dp_cool + p_c
eta_po = 0.7
eta_pf = 0.7


#環境についてのパラメタ
R_0 = 8314.3 # J/(kmolK) 
gam = 1.4
c_p = gam / (gam-1) * R_0 #定圧モル比熱


G = sp.Symbol("G")
a = sp.Symbol("a")
G_gf = G
G_cf = a*G
G_go = MR_g*G
G_co = a*MR_c*G


eq = (G_co + )
