import numpy as np
import sympy
from matplotlib import pyplot as plt

#課題２より#############################################

Isp = 416.9388876840935
f_in = 0.09496404977066682
g_0 = 9.8 # m/s2
dV = 7000 # m/s
F = 270248.8057814671 #N

#環境についてのパラメタ
R_0 = 8314.3 # J/(kmolK) 
gam = 1.4 #比熱比

#推進剤に関するパラメタ
#酸化剤　F2
W_o = 38# 単位[kg/kmol]　酸化剤剤分子量
rho_o = 1510# 単位[kg/m3]　酸化剤密度

#燃料　H2
W_f = 2# 単位[kg/kmol]　燃料分子量
rho_f = 71# 単位[kg/m3]　燃料密度

#燃焼室
p_c = 10e6 #燃焼室圧力　Pa
MR_c = 4.4 #燃焼室質量混合比(o/f)

######################################################

#ガスジェネレータ
MR_g = 19/8 #ガスジェネレータ質量混合比(o/f) 化学量論比の1/8
p_g = sympy.Symbol("p_g") #ガスジェネレータ圧力
nR = MR_g*W_f/W_o #モル比
M = 1/(1+nR)* W_f + nR/(1+nR)*W_o #ガスジェネレータ内平均分子量

#圧力損失
alpha = 0.2
beta = 0.2
gamma = 0.4

#タービン諸元
p_1 = p_g #タービン入口圧力
p_2 = 1013e2 #タービン出口圧力
T_1 = 780 #タービン入口温度
# T_2 = #タービン出口温度
eta_t = 0.5
C_p = gam / (gam-1) * R_0/M #定圧モル比熱

#ポンプ諸元
eta_po = 0.7
eta_pf = 0.7

#質量流量
a = sympy.Symbol("a")
#G_gfとの比
G_gf = 1
G_cf = a #aの定義
G_go = MR_g
G_co = a*MR_c

#圧力損失
def pressure_loss(p_g):
    dp_ic = alpha*p_c
    dp_ig = beta*p_g
    dp_cool = gamma*p_c
    p_po = dp_ig + p_g
    p_pf = dp_ic + dp_cool + p_c
    return p_po, p_pf




if __name__ == "__main__":    
    p_po, p_pf = pressure_loss(p_g)
    
    #ポンプ駆動とタービン出力のつり合い式
    eq = (G_co + G_go)*p_po/rho_o/eta_po + (G_cf + G_gf)*p_pf/rho_f/eta_pf - (G_go + G_gf)*C_p*eta_t*T_1*(1-(p_2/p_1)**((gam-1)/gam))
    fa = sympy.solve(eq,a)
    print(fa[0])
    
    #グラフ描画
    pg_lst = np.linspace(1e6,20e6,100)
    alst = []
    for val in pg_lst:
        alst.append(float(fa[0].subs(p_g,val)))
    fig, ax = plt.subplots()
    ax.plot(pg_lst, alst)
    ax.set_xlabel("p_g")
    ax.set_ylabel("a")
    ax.grid()
    plt.show()
    
    #最適化
    a_max = max(alst)
    id =alst.index(a_max)
    p_g = pg_lst[id]
    print(f"p_g:{p_g}")

    #outputs
    p_po, p_pf = pressure_loss(p_g)    
    print(f"p_po:{p_po}")
    print(f"p_pf:{p_pf}")

    m_1 = a_max + a_max*MR_c #燃焼室に向かう質量流量
    m_2 = 1 + MR_g #タービンに向かう質量流量
    Isp = Isp*m_1/(m_1+m_2)
    print(f"Isp:{Isp}")
    
    

    V_j = Isp*g_0
    PR = (np.exp(-dV/V_j) - f_in)/(1-f_in)
    print(f"PR:{PR*100}%")
    
    F = F*m_1/(m_1+m_2)
    print("F", F)
