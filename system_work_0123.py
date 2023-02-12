m=1
l=1
g=9.8

from math import sin, cos, pi
from matplotlib import pyplot as plt



def deriv_damp_osc(t,xlst):
    theta=xlst[0]
    phi=xlst[1]
    thetadot=xlst[2]
    phidot=xlst[3]
    dx = [thetadot,
          phidot,
          3*(6*g*sin(theta)\
              -3*g*cos(theta-phi)*sin(phi)\
                  +6*l*thetadot**2*cos(theta-phi)*sin(theta-phi)\
                      +4*l*phidot**2*sin(theta-phi))\
                          /(2*l*(9*cos(theta-phi)**2-16)),
          -3*(9*g*cos(theta-phi)*sin(theta)\
              -8*g*sin(phi)\
                  +16*l*thetadot**2*sin(theta-phi)\
                      +6*l*phidot**2*cos(theta-phi)*sin(theta-phi))\
                          /(2*l*(9*cos(theta-phi)**2-16))
        ]
    return dx

# ルンゲクッタ法(4次)で減衰振動を計算する関数
def solve_damp_osci_rk4(t_end,dlt):
  # 各時刻のx,xdotの値を格納するリスト
  # 初期値 x=[1.0,1.0] を設定
  t,x = 0,[pi/4,0,0,0]
  lst_theta,lst_phi,lst_thetadot,lst_phidot,lst_t = [x[0]],[x[1]],[x[2]],[x[3]],[t]
  # ループ
  for i in range(int(t_end/dlt)):
    # tでの傾きを計算
    k1 = deriv_damp_osc(t,x)
    # 時刻 t/2 だけ進んだところでの傾きを計算
    k2 = deriv_damp_osc(t+0.5*dlt,[x[j]+0.5*dlt*k1[j] for j in range(4)])
    # もう1回時刻 t/2 だけ進んだところでの傾きを計算
    k3 = deriv_damp_osc(t+0.5*dlt,[x[j]+0.5*dlt*k2[j] for j in range(4)])
    # t 進んだところでの傾き
    k4 = deriv_damp_osc(t+dlt,[x[j]+dlt*k3[j] for j in range(4)])
    # 次の時刻のx,xdot,tの値を更新(1/6公式)
    for j in range(4):
      x[j] += dlt/6 * (k1[j]+2*k2[j]+2*k3[j]+k4[j])
    t += dlt
    # リストに追加
    lst_theta.append(x[0])
    lst_phi.append(x[1])
    lst_thetadot.append(x[2])
    lst_phidot.append(x[3])
    lst_t.append(t)
  # 時刻リスト, xのリスト, x-dotのリストを返す
  return lst_t, lst_theta, lst_phi, lst_thetadot, lst_phidot

# ルンゲクッタ法を実行
lst_trk, lst_thetark, lst_phirk, lst_thetadotrk, lst_phidotrk = solve_damp_osci_rk4(10.0,0.1)

# プロット
fig1,ax1=plt.subplots()
ax1.plot(lst_trk, lst_thetark,c='b', label='theta (Runge-Kutta)')
ax1.plot(lst_trk, lst_phirk, c='r', label='phi (Runge-Kutta)')
ax1.set_xlabel('t/s')
ax1.set_ylabel('θ,Φ/rad')
plt.legend()
plt.show()


#運動エネルギーと位置エネルギー
'''Klst=[0.5*m*l**2*thetadot**2 \
    + 0.5*m*l**2*(thetadot**2+phidot**2\
        +2*thetadot*phidot*cos(theta-phi))\
            for (theta,phi,thetadot,phidot) in zip(lst_thetark, lst_phirk, lst_thetadotrk, lst_phidotrk)]

Ulst=[-m*g*l*cos(theta)-m*g*l*(cos(theta)+cos(phi))\
    for (theta, phi) in zip(lst_thetark, lst_phirk)]


Elst=[k-u for (k,u) in zip(Klst,Ulst)]
'''

'''
Klst=[]
Ulst=[]
Elst=[]
for i in range(len(lst_trk)):
    theta=lst_thetark[i]
    phi=lst_phirk[i]
    thetadot=lst_thetadotrk[i]
    phidot=lst_phidotrk[i]
    
    Klst.append(
        0.5*m*(2*l)**2*thetadot**2\
        + 0.5*m*(2*l)**2*(thetadot**2+phidot**2\
            +2*thetadot*phidot*cos(theta-phi))
        )
    
    Ulst.append(
        -m*g*2*l*cos(theta)\
            -m*g*2*l*(cos(theta)+cos(phi))
            )
    Elst.append(Klst[i]+Ulst[i])
'''

Klst=[]
Ulst=[]
Elst=[]
for i in range(len(lst_trk)):
    theta=lst_thetark[i]
    phi=lst_phirk[i]
    thetadot=lst_thetadotrk[i]
    phidot=lst_phidotrk[i]
    
    Klst.append(
        m*l**2*thetadot**2*2/3\
            +m*l**2*phidot**2/6\
                +m*l**2*(4*thetadot**2+4*cos(theta-phi)*thetadot*phidot+phidot**2)/2
        )
    
    Ulst.append(
        -m*g*l*cos(theta)\
            -m*g*(2*l*cos(theta)+l*cos(phi))
            )
    Elst.append(Klst[i]+Ulst[i])


fig2,ax2=plt.subplots()
ax2.plot(lst_trk, Klst, c='r', label=('Kinetic Energy'))
ax2.plot(lst_trk, Ulst, c='b', label=('Potential Energy'))
ax2.plot(lst_trk, Elst, c='g', label=('Total Energy'))
plt.legend()
plt.show()

#アニメーション
import matplotlib.animation as animation

fig3,ax3=plt.subplots()
ims=[]
ax3.set_xlim(-4,4)
ax3.set_ylim(-5,0.5)
ax3.set_aspect('equal')
ax3.grid()
legend=True

x1lst=[2*l*sin(theta) for theta in lst_thetark]
y1lst=[-2*l*cos(theta) for theta in lst_thetark]
x2lst=[2*l*sin(theta)+2*l*sin(phi) for (theta,phi) in zip(lst_thetark, lst_phirk)]
y2lst=[-2*l*cos(theta)-2*l*cos(phi) for (theta,phi) in zip(lst_thetark, lst_phirk)]

'''
for i in range(len(lst_trk)):
  im=ax2.plot([0,x1lst[i]],[0,y1lst[i]],'-',color='b',label='B1')
  ims.append(im)
  im=ax2.plot([x1lst[i],x2lst[i]],[y1lst[i],y2lst[i]],'-',color='r',label='B2')
  ims.append(im)
  if legend:
    plt.legend(loc='upper left')
    legend=False
'''

line1, = ax3.plot([], [], '-', c='b', lw=4, label='B1')
line2, = ax3.plot([], [], '-', c='r', lw=4,  label='B2')
time_template = 'time = {:.1f}sec'
time_text = ax3.text(0.05, 0.9, '', transform=ax3.transAxes)

def animate(i):
    line1.set_data([0,x1lst[i]],[0,y1lst[i]] )
    line2.set_data([x1lst[i],x2lst[i]],[y1lst[i],y2lst[i]])
    time_text.set_text(time_template.format(lst_trk[i]))
    return line1,line2, time_text


ani = animation.FuncAnimation(fig3, animate, range(len(lst_trk)),
                              interval=100, blit=True)
plt.legend()
#ani=animation.ArtistAnimation(fig2,ims,interval=100, blit=True)
plt.show()
