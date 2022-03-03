from turtle import *
speed(0)
colormode(255)
shade = 255
for i in range(50):
    fillcolor(shade,shade,shade)
    begin_fill()
    left(360//50)
    for side in range(4):
        forward(150)
        left(90)
    end_fill()
    shade -= 255//50
done()