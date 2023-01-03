print(1.225*0.836*((300*(10**3)/60/60)**2)/2/9.8)


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig,ax=plt.subplots()
ims=[]
ax.set_aspect('equal')
plt.grid()
legend=True

for i in np.linspace(0,5*np.pi,100):
  omega=365.25/248.7
  x=np.cos(i)
  y=np.sin(i)
  im=ax.plot(x,y,'o',color='b',label='earth')
  ims.append(im)
  x=np.cos(omega*i)
  y=np.sin(omega*i)
  im=ax.plot(x,y,'o',color='r',label='planet')
  ims.append(im)
  if legend:
    plt.legend(loc='upper left')
    legend=False
  

ani=animation.ArtistAnimation(fig,ims,interval=10)
plt.show()