# Andre Meronen 08.10.2024
# Harjutus 2
# Olümpiamängud

import turtle
aken = turtle.Screen()
aken.setup(width=800, height=600)
aken.title("sinilill - Andre Meronen")
turtle.speed("fastest")
turtle.pensize(10)


#vars
turtle.pencolor("green")
turtle.left(90)
turtle.fd(-150)
turtle.fd(200)

#õis
turtle.begin_fill()
turtle.color("blue","lightblue")
turtle.right(90)
turtle.circle(60)
turtle.end_fill()

turtle.left(90)
turtle.penup()
turtle.fd(50)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow","yellow")
turtle.right(90)
turtle.circle(10)
turtle.end_fill()

#leht
turtle.begin_fill()
turtle.color("green","green")
turtle.penup()
turtle.goto(-20,-50)
turtle.pendown()
turtle.left(90)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.end_fill()


turtle.done()