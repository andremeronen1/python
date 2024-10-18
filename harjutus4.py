#16.10.24 Andre Meronen
#Ülesanne 4

# 5. Ringi pindala ja turtle
import turtle

try:
    r = int(input("Lisa ringi raadius: "))
    pi = 3.14
    s = pi*r**2
    p = 2*pi*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f} ")
    turtle.circle(r, 360)
    turtle.done

except:
    print("Tegid sisestamisel vea!")











"""
# 4. Kingituste pakkimine
try:
    kingitused = int(input("Lisa kinkide arv: "))
    maht = int(input("Lisa kinkide maht: "))
    pakid = kingitused // maht
    yle = kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Tegid sisestamisel vea!")
"""

"""
# 3. faili allalaadimine
try:
    failisuurus = int(input("Sisesta failisuurus (MB): "))
    downKiirus= int(input("Sisesta allalaadimiskiirus (MB/S): "))
    aeg = failisuurus / downKiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("Tegi sisestamisel vea!")
"""




"""
# 2. Raamatute allahindlus
ale = 0.3
kogus = 3
hind = 12.53
summa = hind - (hind * ale) * kogus
print(f"3 raamatu hind soodusega on {summa:0.2f}€")
"""

"""
# 1. Aia pikkus
a = int(input( "Sisesta külg 1: "))
b = int(input( "Sisesta külg 2: "))
p = 2 * (a + b)
print(f"Aia kogupikkus on {p} meetrit.")
"""