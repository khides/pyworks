import turtle
import kame

turtle.setup(750,750,0,0)
hist_kame=kame.Kame()
hist_kame.draw_bar(120)

hist_kame.histogram(hist_data)

turtle.done()