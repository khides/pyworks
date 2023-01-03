import turtle
turtle.setup(750,750,0,0)
kame=turtle.Turtle()


###三角形を描く
for i in range(3):
    kame.forward(200)
    kame.left(120)


###五芒星を描く
kame.home()
kame.clear()
for i in range(5):
    kame.forward(200)
    kame.left(144)

###ランダムに動かす
kame.home()
kame.clear()

kame.penup()
kame.forward(100)
kame.left(90)
kame.pendown()
kame.circle(100)
kame.penup()
kame.home()
kame.pendown()
import random
while kame.distance(0,0)<100:
    kame.left(random.randint(1,360))
    kame.forward(15)


kame.home()
kame.clear()

kame.penup()
kame.forward(100)
kame.left(90)
kame.pendown()
kame.circle(100)
kame.penup()
kame.home()
kame.pendown()

import random
while True:
    kame.left(random.randint(1,360))
    kame.forward(15)
    if kame.distance(0,0)>100:
        kame.undo()

turtle.done()