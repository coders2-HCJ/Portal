import turtle
t = turtle.Turtle()
t.penup()
t.left(90)
t.back(100)
t.left(90)

def dp(ns, ss):
    t.pendown()
    for i in range(ns):
        t.forward(ss)
        t.right(360/ns)

def portal(rep, ss):
    for i in range(rep):
        dp(i + 3, ss)

t.pencolor("#00FFD6")
portal(18, 50)
