def center_circle(r=150):
    import turtle
    turtle.setup(750,750,0,0)

    kame=turtle.Turtle()
    kame.shapesize(2,2,1)

    kame.penup()
    kame.forward(r)
    kame.pendown()
    kame.left(90)
    kame.circle(r)
    kame.penup()
    kame.home()
    kame.pendown()



center_circle(200)

center_circle(150)

def center_circle2(kame,r=150):
    kame.penup()
    kame.forward(r)
    kame.pendown()
    kame.left(90)
    kame.circle(r)
    kame.penup()
    kame.home()
    kame.pendown()


import turtle
turtle.setup(750,750,0,0)
kame=turtle.Turtle()
kame.shapesize(2,2,1)

center_circle2(kame,250)

turtle.done()