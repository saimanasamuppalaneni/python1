import turtle
win=turtle.Screen()
win.screensize(400,400)
win.title("star")
win.bgcolor('beige')
t=turtle.Turtle()
t.color("black")
t.width(5)
n=3
a=120
t.fillcolor("aqua")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(a)
t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(100)
    t.right(a)
t.end_fill()
turtle.done()
    
