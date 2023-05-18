import numpy as np
from matplotlib import pyplot as plt

#環境に関するパラメタ
g_0 = 9.8 # m/s2
dV = 7000 # m/s
m_L = 2000 # kg ペイロード質量
g_i = 0.3 * g_0 
rho_s = 300 # kg/m3 標準推進剤平均密度
f_ins = 0.1
T_0 = 298.15 # K　標準状態温度
T_i = 300 # K　燃焼前温度
gam = 7/5 #比熱比
R_0 = 8314.3 # J/(kmolK) 
c_p = gam / (gam-1) * R_0 #定圧モル比熱
eta_j = 0.96 #ノズル効率
p_a = 10 * 1000 # Pa　大気圧
ts = 10/1000 # s　燃焼室滞在時間

#推進剤に関するパラメタ
#酸化剤　F2
W_o = 38# 単位[kg/kmol]　酸化剤剤分子量
rho_o = 1510# 単位[kg/m3]　酸化剤密度
dH_o = 0# 単位は[J/kmol]　酸化剤標準生成エンタルピー
#燃料　H2
W_f = 2# 単位[kg/kmol]　燃料分子量
rho_f = 71# 単位[kg/m3]　燃料密度
dH_f =0 # 単位[J/kmol]　燃料標準生成エンタルピー
#生成物
W_p = 20 # 単位[kg/kmol]
dH_p = -271.2e6# 単位[J/kmol]
coef_th = {'H2':1, 'F2':1, 'HF':2} #反応式の係数
# 無次元量　推進剤質量混合比　酸化剤/燃料

#燃焼室のパラメタ
p_0 = 10e6# 単位[Pa]
k = 5# 燃焼器スロート断面積比A1/At
d_t = 2# タンク直径 単位[m]


##数値計算
def flag(MR):
    fuel_rich_flag = True #fuel rich True
    nR = initial(MR)[2] #モル比　酸化剤/燃料
    coef_r = coef_th['H2']/coef_th['F2'] #係数比　燃料/酸化剤
    if nR >coef_r:
        fuel_rich_flag = False
    return fuel_rich_flag

def initial(MR):
    nR = MR*W_f/W_o #モル比　酸化剤/燃料
    n_fr = 1/(1+nR)
    n_or = nR/(1+nR)#モル分率    
    coef_r = coef_th['H2']/coef_th['F2'] #係数比　燃料/酸化剤    
    n_total = 1
    nf_i = n_total*n_fr
    no_i = n_total*n_or
    return nf_i,no_i,nR,coef_r    

def reaction(MR):
    fuel_rich_flag = flag(MR)
    nf_i,no_i,nR,coef_r = initial(MR)
    if fuel_rich_flag:
        n_rest_f = nf_i - no_i*coef_r
        n_rest_o = 0
        n_p = no_i*coef_th['HF']/coef_th['F2']
        M = n_rest_f*W_f + n_p*W_p
    else:
        n_rest_f = 0
        n_rest_o = no_i - nf_i/coef_r
        n_p = nf_i*coef_th['HF']/coef_th['H2']
        M = n_rest_o*W_o + n_p*W_p
        
    return n_rest_f,n_rest_o,n_p,M

def get_Tf(MR):
    nf_i,no_i,nR,coef_r = initial(MR)
    n_rest_f,n_rest_o,n_p,M =reaction(MR)
    
    c_p = gam/(gam-1)*R_0
    A = nf_i*dH_f + no_i*dH_o
    B = n_rest_f*dH_f + n_rest_o*dH_o + n_p*dH_p
    a = c_p*(n_rest_f + n_rest_o + n_p)
    b = c_p*(T_0 - T_i)*(nf_i + no_i) - c_p*T_0*(n_p + n_rest_f + n_rest_o)

    T_f = (A - B - b)/a
    if T_f>2500:
        T_f =  2500*(A - 2*B - b)/(2500*a - B)
    return T_f
    
def get_Isp(MR,p_0):
    M = reaction(MR)[3]
    C_p = c_p/M
    T_f = get_Tf(MR)
    p_j = p_a
    V_j = np.sqrt(2*eta_j*C_p*T_f*(1-(p_j/p_0))**((gam-1)/gam))
    Isp = V_j/g_0
    return Isp
    
def get_fin(MR):
    rho = (1 + MR)/(1/rho_f + MR/rho_o)
    f_in = (1/f_ins-1)*rho/rho_s + 1
    f_in = 1/f_in
    return f_in,rho

def get_PR(MR,p_0):
    V_j = get_Isp(MR,p_0)*g_0
    f_in = get_fin(MR)[0]
    PR = (np.exp(-dV/V_j) - f_in)/(1-f_in)
    return PR
    

##グラフ描画
MR_lst = np.arange(0,30,0.1)
PR_lst = []
Tf_lst = []
Isp_lst = []
fin_lst = []
for val in MR_lst:
    PR_lst.append(get_PR(val,p_0))
    Tf_lst.append(get_Tf(val))
    Isp_lst.append(get_Isp(val,p_0))
    fin_lst.append(get_fin(val)[0])

result = [PR_lst,Tf_lst,Isp_lst,fin_lst]
name = ['PR','Tf','Isp','fin']
fig = plt.figure(figsize=(15,10))
for i in range(4):
    ax = fig.add_subplot(2,2,i+1)
    ax.plot(MR_lst,result[i])
    ax.set_title(name[i])   
    ax.grid()
plt.savefig('vs_MR.pdf')
plt.show()


##ペイロード比の最大値と、その時の質量混合比
maxPR = max(PR_lst)
print(maxPR)
PRidx = PR_lst.index(maxPR)
print(PRidx)
maxMR = MR_lst[PRidx]
print(maxMR)

##燃焼室及びタンク寸法の数値計算
def get_L(MR):
    M = reaction(MR)[3]
    T_F = get_Tf(MR)
    L = ts/np.sqrt(M/(gam*R_0*T_F)*((gam+1)/2)**((gam+1)/(2*(gam-1))))/k
    return L

def get_D(MR,p_0):
    p_j = p_a
    CF = np.sqrt(2*gam**2/(gam-1)*(2/gam+1)**((gam+1)/(gam-1))*(1-(p_j/p_0)**((gam+1)/(2*(gam-1)))))
    PR = get_PR(MR,p_0)
    At = m_L/PR*(g_0+g_i)/CF/p_0    
    A1 = k*At
    D = 2*np.sqrt(A1*np.pi)
    return D

def get_L_t(MR):
    PR = get_PR(MR,p_0)
    fin,rho = get_fin(MR)
    mp = (1-PR)*(1-fin)*m_L/PR
    L_t = mp/rho/np.pi*4/(d_t**2)
    return L_t

print(get_L(maxMR),get_D(maxMR,p_0),get_L_t(maxMR))


##燃焼室圧力変化
p_0lst = np.linspace(10e5,20e6,1000)
MR = 4.1
PR_lst = []
Tf_lst = []
Isp_lst = []
fin_lst = []
for val in p_0lst:
    PR_lst.append(get_PR(MR,val))
    Tf_lst.append(get_Tf(MR))
    Isp_lst.append(get_Isp(MR,val))
    fin_lst.append(get_fin(MR)[0])

result = [PR_lst,Tf_lst,Isp_lst,fin_lst]
name = ['PR','Tf','Isp','fin']
fig = plt.figure(figsize=(15,10))
for i in range(4):
    ax = fig.add_subplot(2,2,i+1)
    ax.plot(p_0lst,result[i])
    ax.set_title(name[i])   
    ax.grid()

plt.savefig('vs_p_0.pdf')
plt.show()