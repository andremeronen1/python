#06.11.2024 Andre Meronen
#Harjutus 9.14
import turtle 
d = 100
a = 120
b = 60
turtle.speed(0)

for i in range(6):
    turtle.lt(a)
    turtle.rt(b)
    for i in range(3):
        turtle.fd(d/2)
        turtle.left(a)



turtle.penup()
turtle.goto(d,0)
turtle.pendown()
for i in range(4):
    turtle.fd(d)
    turtle.lt(90)

turtle.penup()
turtle.goto(125,0)
turtle.pendown()
turtle.pencolor("Red")
for i in range(4):
    turtle.fd(d/2)
    turtle.lt(90)

turtle.penup()
turtle.goto(d,d)
turtle.pencolor("Green")
turtle.pendown()
for i in range(3):
    turtle.fd(d)
    turtle.lt(a)

turtle.penup()
turtle.goto(350,0)
turtle.pendown()

k = 5 

for i in range(5):
    turtle.fd(d/2)
    turtle.lt(120)
    for i in range(2):
        turtle.fd(d)
        turtle.lt(120)
    turtle.fd(d/2)
    turtle.lt(360/k)









turtle.done