import numpy as np
import sympy
from matplotlib import pyplot as plt

#課題２より#################################################
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

############################################################

#プリバーナ
MR_b = 19/8 #ガスジェネレータ質量混合比(o/f) 化学量論比の1/8
p_b = sympy.Symbol("p_b") #プリバーナ圧力
nR = MR_b*W_f/W_o
M = 1/(1+nR)* W_f + nR/(1+nR)*W_o

#圧力損失
alpha = 0.2
beta = 0.2
gamma = 0.4

#タービン
p_1 = p_b #タービン入口圧力
#p_2 = 
T_1 = 1000 #タービン入口温度
# T_2 = #タービン出口温度
eta_t = 0.75
C_p = gam / (gam-1) * R_0/M #定圧モル比熱

#ポンプ
eta_pdo = 0.7
eta_po = 0.7
eta_pf = 0.7

#質量流量
G_bf = 1
G_cf = G_bf
G_bo = MR_b
G_co = G_cf*MR_c - G_bo
G_f = G_cf

#圧力損失
def pressure_loss(p_b):
    dp_ic = alpha*p_c
    dp_ib = beta*p_b
    dp_cool = gamma*p_c
    p_pf = dp_cool + dp_ib + p_b
    p_2 = p_c +dp_ic #タービン出口圧力
    p_po = dp_ic + p_c
    dp_pdo = dp_ib + p_b - p_po
    return dp_pdo, p_po, p_pf, p_2


if __name__ == "__main__":
    dp_pdo, p_po, p_pf, p_2 = pressure_loss(p_b)

    #ポンプ駆動とタービン出力のつり合い式
    eq = G_bo*dp_pdo/rho_o/eta_pdo + (G_co + G_bo)*p_po/rho_o/eta_po + G_f*p_pf/rho_f/eta_pf - (G_bo + G_bf)*C_p*eta_t*T_1*(1-(p_2/p_1)**((gam-1)/gam))
    # fa = sympy.solve(eq,p_b)
    # print(fa[0])
    
    #グラフ描画
    pb_lst = np.linspace(1e6, 5e7, 100)
    vallst = []
    for val in pb_lst:
        vallst.append(eq.subs(p_b,val))
    fig, ax = plt.subplots()
    ax.plot(pb_lst, vallst)
    ax.grid()
    plt.show()
    
    #二分法で解を見つける
    mn = 1e7
    mx = 1.5e7
    mean = (mn + mx)/2
    while abs(eq.subs(p_b, mean)) > 10**-6:
        mean = (mn + mx)/2
        if eq.subs(p_b, mean)< 0 :
            mx = mean
        else :
            mn = mean
    p_b = mean
    print(f"p_b:{p_b}")  
    
    #outputs
    dp_pdo, p_po, p_pf, p_2 = pressure_loss(p_b)
    print(f"p_po:{p_po}")
    print(f"p_pf:{p_pf}")

    #推力、ペイロード比は変化なし