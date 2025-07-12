import turtle
win=turtle.Screen()
win.screensize(400,400)
win.title("spiral square")
win.bgcolor('black')
t=turtle.Turtle()
t.color("goldenrod")
x=5
while True:
    t.forward(x)
    t.right(90)
    x+=3

