import itertools
import math



alpha = 20 #[degree]圧力角
mi = 4 #[mm]１と２のモジュール
mo = 6 #[mm]３と４のモジュール
fw = 0.74 #荷重係数
fb = 3 #歯幅係数　3~5
k = 0.053*9.8 #[N/mm^2]触面応力係数
sigma = 60 #[N/mm^2]許容曲げ応力
ydic = {17:0.33, 18:0.335, 19:0.34, 20:0.364, 21:0.352, 22:0.354, 24:0.359, 26:0.367, 28:0.372, 30:0.377, 34:0.388, 38:0.4,
        43:0.411, 50:0.422, 60:0.433, 75:0.443, 100:0.454, 150:0.464}



slst =list(range(16,30))
blst = list(range(50,100))

glst = []
for a,b,c,d in itertools.product(slst,blst,slst,blst):
    if mi*(a + b) - mo*(c + d) == 0:
        if 20-0.1<(b*d)/(a*c)<20+0.1:
            if math.gcd(a,b) == 1:
                if math.gcd(c,d) == 1:
                    glst.append([a,b,c,d]) #入出力軸のずれなし、ギア比が19.9以上20.1以下、１と２、３と４が互いに素
print(glst)



def vi(z): #１と２の歯速[m/s]
    return 25*math.pi*z*mi/1000
def vo(z): #３と４の歯速[m/s]
    return 1.25*math.pi*z*mo/1000
def fv(v): #バースの速度係数
    if v<5:
        return 3.05/(3.05+v)
    else:
        return 6.1/(6.1+v)
    
    
def y(z):
    while z not in ydic: #安全側にとるため、該当値があるまで減算
        z -= 1
    return ydic[z]

def forcel(v,m,z): #曲げ応力　ルイスの式に従う
    return (fw*fv(v)*sigma)*m*(fb*math.pi*m)*y(z)
def forceh(v,m,za,zb): #面圧強さ
    return fv(v)*k*m*(fb*math.pi*m)*2*za*zb/(za+zb)

finlst = []
for lst in glst:
    if forcel(vi(lst[0]),mi,lst[0]) > 3700/vi(lst[0]):
        if forcel(vo(lst[3]),mo,lst[2]) > 3700/vo(lst[3]):
            if forceh(vi(lst[0]),mi,lst[0],lst[1]) > 3700/vi(lst[0]):
                if forceh(vo(lst[3]),mo,lst[2],lst[3]) > 3700/vo(lst[3]):
                    finlst.append(lst)

for lst in finlst:
    print(lst)
