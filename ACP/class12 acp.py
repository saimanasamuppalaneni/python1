# square
import turtle
win=turtle.Screen()
win.screensize(400,400)
win.title("square")
win.bgcolor('plum')
t=turtle.Turtle()
t.color("darkslategray")
t.width(5)
n=6
a=60
t.fillcolor("plum")
t.begin_fill()
for i in range(n):
    t.forward(90)
    t.left(90)
t.end_fill()
turtle.done()