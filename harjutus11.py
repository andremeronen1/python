#08.11.2024 Andre Meronen
#Harjutus 11
import turtle
import random

def viisnurk(k):
    for j in range(k):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,180))
        for i in range(5):
            turtle.fd(100)
            turtle.lt(72)

def ring(k):
    for j in range(k):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        for i in range(1):
            turtle.circle(100)
            

    

def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)

def suvaline(k):
    for i in range(k):
        turtle.speed(0)
        my_list=[viisnurk, ring, ruut]
        random.choice(my_list)(1)
        
loop=1

while loop==1:
    try:
        valik = int(input("1 - viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nLisa valik (1-4):"))
        kujunditeArv = int(input("Mitu kujundit soovid joonistada: "))
    except:
        print("Game Over")
        loop = 0 
        break
if valik =="" or kujunditeArv=="":
    print("Game Over")
    loop = 0
if valik == 1:
    viisnurk(kujunditeArv)
elif valik == 2:
    ring(kujunditeArv)
elif valik == 3:
     ruut(kujunditeArv)
else:
    suvaline(kujunditeArv)






# def sarnased_esitahed(nimi):
#     tykk = nimi.split(" ")
#     if tykk[0][0] == tykk[1][0]:
#         return True
#     else:
#         return False
    
    
    
    




# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False
















# def kolm_pikimat_sona(a):
#     sonastik = {}
#     for i in a:
#         sonastik[i] = len(i)
#     sorteeritud = sorted(sonastik.items(), key = lambda x:x[1], reverse = True)
#     for j in range(3):
#         print(sorteeritud[j][0])


# sonad = ["üks", "kaks", "kolmsada", "üksmiljonsadamust"]


# kolm_pikimat_sona(sonad)














# def pikim_sona(*sonad):
#     pikim = 0
#     for i in sonad:
#         if len(i)>pikim:
#             pikim=len(i)
#     print(f"Pikim sõna on {pikim} märki!")

# pikim_sona("üks", "kaks", "kolkümmend")









turtle.done()