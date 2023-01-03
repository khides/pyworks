import ita
image=[[0,0,1,1],[0,1,0,1],[1,1,0,0]]
ita.plot.image_show(image)


import ita
def draw_area(image,color):
    for i in range(0,len(image)):
        for j in range(0,len(image[0])):
            if i/100>=(j/100)**2 and j/100>=(i/100)**2:
                image[i][j]=color
    return image
image=ita.array.make3d(150,150,3)
c=[0.0,1.0,1.0]
image=draw_area(image,c)
ita.plot.image_show(image)



import ita
def draw_figure(image):
    n=len(image)
    m=len(image[0])
    for i in range(0,n):
        for j in range(0,m):
            image[i][j]=[2*(j/n-0.5)*(i/m-0.5)+0.5,i/n,j/m]
    return image
image=ita.array.make3d(150,150,3)
ita.plot.image_show(draw_figure(image))


def draw_circle(image,b,a,r,color):
    for y in range(0,len(image)):
        for x in range(0,len(image[0])):
            if (x-a)**2+(y-b)**2<r**2:
                image[y][x]=color
    return image
image=ita.array.make3d(200,200,3)
c=[0.0,1.0,1.0]
image=draw_circle(image,100,100,50,c)
ita.plot.image_show(image)


