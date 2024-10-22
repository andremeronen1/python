#18.10.24 Andre Meronen
# Ülesanne 5
import random
import turtle 




# 4. Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
suv = random.randint(0,1)
kasutaja_valik = input("Kull või kiri: ")
if suv==1 and kasutaja_valik=="kull":
    varv = "green"
else:
    varv = "red"
turtle.color(varv)
turtle.circle(50,360)
turtle.done







# 3. Matemaatika test (randit)
a, b = random.randint(1,10), random.randint(1,10)
vastus = int(input(f"Lisa vastus {a}*{b}="))
if vastus == a*b:
    print("Tubli!")
else:
    print("Loll oled!")




# 2. Ilmaennustuste rakendus (and)
c = 15
if c < 0:
    print("Talveriided")
elif c >= 0 and c <=15:
    print("Kevad-sügis")
else:
    print("Suvi")




# 1. Vanusepiiranguga üritus
vanus = 18
if vanus >= 18:
    print("Saab sisse!")
else:
    print("Liiga noor!")
