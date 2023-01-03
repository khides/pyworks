def pm_step(y,x,vy,vx,stride):
  #(x,y):  現在の位置
  #(vx,vy):現在の速度ベクトル
  #stride:時間刻み幅
  g=9.8
  x=x+vx*stride
  y=y+vy*stride
  vx=vx
  vy=vy-g*stride
  return [y,x,vy,vx]

def parabolic_motion(y,x,vel_y,vel_x):
  stride=0.3
  cur=[y,x,vel_y,vel_x]
  result=[]
  while (0<=cur[0]<100 and 0<=cur[1]<100):
    result.append(cur)
    cur=pm_step(cur[0],cur[1],cur[2],cur[3],stride)
  return result

def draw_circle(image,y,x,r,color):
  for i in range(0,len(image)):
    for j in range(0,len(image[0])):
      if (y-i)**2+(x-j)**2<r**2:
        image[i][j]=color
  return image

import ita
def parabolic_motion_ball(y,x,vy,vx):
  res=parabolic_motion(y,x,vy,vx)
  images=ita.array.make1d(len(res))
  for i in range(0,len(res)):
    im=ita.array.make2d(100,100)
    cur_y=99-round(res[i][0])
    cur_x=round(res[i][1])
    draw_circle(im,cur_y,cur_x,5,1)
    images[i]=im
  return images

from matplotlib import pyplot as plt
ani=parabolic_motion_ball(0,0,40,12)
anim=ita.plot.animation_show(ani)
plt.show()