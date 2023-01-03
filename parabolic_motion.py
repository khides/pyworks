import ita
from matplotlib import pyplot as plt
import copy

#中心点座標を指定して塗りつぶされた円を描く関数
def draw_circle(image,b,a,r,c):
    for y in range(0,len(image)):
        for x in range(0,len(image[0])):
            if (x-a)**2+(y-b)**2<r**2:
                image[y][x]=c
    return image

#現在の位置を指定してΔ秒後の位置を返す関数
def pm_step(y,x,vy,vx,delta):
    g=9.8
    x=x+vx*delta
    y=y+vy*delta
    vx=vx
    vy=vy-g*delta
    return [y,x,vy,vx]


#フェーズごとのボールの位置を格納するリストをつくる関数
def current_point(n,m,y0,x0,vy0,vx0,delta):
    cur=[y0,x0,vy0,vx0]
    result=[]
    while 0<=cur[0]<n and 0<=cur[1]<m:
        result.append(cur)
        cur=pm_step(cur[0],cur[1],cur[2],cur[3],delta)
    return result

#フェーズごとのボールの位置にボールが描かれたイメージを作成し、
# それらのイメージを格納するリストを作る関数
def parabolic_motion(n,m,y0,x0,vy0,vx0,delta=0.3,r=5,c=[0.0,1.0,1.0]):
    res=current_point(n,m,y0,x0,vy0,vx0,delta)
    image=ita.array.make1d(len(res)) #1カットごとの画像の格納庫
    for i in range(0,len(res)):
        if i==0:
            im=ita.array.make3d(n,m,3) #画像の情報設定(縦、横、カラーの有無)    
        elif i >=1:
            im=copy.deepcopy(image[i-1])#一つ前のフェーズをコピー
            for y in range(len(im)):
                for x in range(len(im[0])):
                    if im[y][x]!=[0.0,0.0,0.0]:
                        im[y][x]=[1.0,1.0,1.0] #軌跡を作る
        cur_y=n-round(res[i][0]) #計算を軽くする為の丸め込み
        cur_x=round(res[i][1])
        draw_circle(im,cur_y,cur_x,r,c)
        image[i]=im
    return image


#実行
ani=parabolic_motion(100,100,0,0,40,12)
anim=ita.plot.animation_show(ani)
plt.show()

