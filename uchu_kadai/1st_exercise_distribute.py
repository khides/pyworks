'''
液体燃料ロケットエンジンは、推力 F=100,000 [lb]（海抜高度）、推進剤消費率 w˙=369.3 [lb/s] 、
推力室出口面積 Ae=760.8 [in 2 ] 、ガス出口平均静圧 pe=10.7 [psia] 、環境圧力 pa=14.7 [psia] （海抜高度）、
重力定数 g=32.2 [ft/s 2 ] で表されます。
ノズルの出口圧力は正弦波状に分布し、壁面での値は平均値の約 2 倍、ノズル軸での値は壁面圧力の 10%のオーダーとなります。
このとき、平均出口圧力peは、次式で求められる一次元出口圧力の代わりとなる。
F=w˙gve+Ae(pe-pa) (1)
上式から、（a）ガス排気速度、（b）真空中のエンジン推力、（c）海面および真空中の有効排気速度を求める。
なお、数値はSI単位で求めている。
'''
F_lb=100000
w_lb_s=369.3
Ae_insquare=760.8
pe_psia=10.7
pa_psia=14.7
g_ft_ssquare=32.2


'''
米国の慣習単位を国際標準単位に変換する。
1in = 0.0254m
1lb=0.454kg
1psia=1lb/in 2 
1ft=0.3048m
'''
in2m=0.0254
lb2kg=0.454
psia2lb_insquare=1
ft2m=0.3048


'''
SI単位でパラメータを求めます。
'''
g=g_ft_ssquare*ft2m
F=F_lb*lb2kg*g
w=w_lb_s*lb2kg
Ae=Ae_insquare*in2m**2
pe=pe_psia*lb2kg/in2m**2*g
pa=pa_psia*lb2kg/in2m**2*g



'''
(a) 式(1)を用いて、veは次のように表される: 
ve=(F-Ae(pe-pa))(g/w˙)
'''
ve=(F-Ae*(pe-pa))/w
print(ve)

'''
(b)真空中の推力は(1)式でpa=0として評価する
'''
Fvac=w*ve+Ae*pe
print(Fvac)

'''
(c) 速度への圧力効果を考慮して有効排気速度を求める。
'''

c0=ve+Ae*(pe-pa)/w
cvac=ve+Ae*pe/w
print(c0,cvac)