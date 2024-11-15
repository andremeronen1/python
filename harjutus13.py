#15.11.2024 Andre Meronen
#Harjutus 13
import turtle
screen = turtle.Screen()
t = turtle.Turtle()

pikkus = screen.numinput("Pikkuse sisestamine", "Kui pika soovid?", default=20, minval=0, maxval=100)
pikkus = 10

for i in range(pikkus*10):
    t.speed(0)
    t.lt(90)
    t.fd(3)
    t.lt(180)
    t.fd(3)
    t.lt(90)
    t.fd(5)
t.goto(0,0)

for i in range(pikkus+1):
    t.lt(90)
    t.fd(5)
    t.write(i, font=("Arial", 10, "normal"))
    t.lt(180)
    t.fd(5)
    t.lt(90)
    t.fd(10*4)
    



print(f"Pikkus on {int(pikkus)} sentimeetrit")



















turtle.done()