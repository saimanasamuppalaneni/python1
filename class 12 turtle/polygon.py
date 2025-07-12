import turtle
win=turtle.Screen()
win.screensize(400,400)
win.title("polygon")
win.bgcolor('hotpink')
t=turtle.Turtle()
t.color("black")
t.width(5)
t.shape('turtle')
n=6
a=60
t.fillcolor("green")
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)
t.end_fill()
turtle.done()
