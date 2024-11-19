#19.11.2024 Andre Meronen
#Harjutus 14
import turtle
ekraan = turtle.Screen()



def muuda_varvi_red():
    turtle.color("red")

def muuda_varvi_green():
    turtle.color("green")

def muuda_varvi_blue():
    turtle.color("blue")

def ruut(x,y):
    print(x,y)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.fd(50)
        turtle.lt(90)

def puhasta_ekraan(x,y):
    turtle.clear()


def vasakKlikk(x, y):
    turtle.goto(x, y)



def keskmineKlikk(x, y):
    turtle.undo()

ekraan.onscreenclick(ruut, 1) 
#ekraan.onscreenclick(paremKlikk, 3) 
ekraan.onscreenclick(puhasta_ekraan, 2) 
ekraan.onkey(muuda_varvi_red, "r")
ekraan.onkey(muuda_varvi_green, "g")
ekraan.onkey(muuda_varvi_blue, "b")


ekraan.listen()
turtle.mainloop()


