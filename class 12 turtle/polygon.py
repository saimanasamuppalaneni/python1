# polygon
import turtle
win=turtle.Screen()
win.screensize(400,400)
win.title("polygon")
win.bgcolor('lightcoral')
t=turtle.Turtle()
t.color("aquamarine")
t.width(5)
n=6
a=60
t.fillcolor("aqua")
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)
t.end_fill()
turtle.done()

