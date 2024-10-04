# Andre Meronen
# 04.10.24
# Harjutus01

# 9. Arvusüsteem
arv = int(input("Lisa 10nd arv: "))
print(bin(arv))
print(hex(arv))


# 10. Kütusekulu arvutamine
liiter = int(input("Lisa kütusekulu: "))
km = int(input("Lisa läbitud kilomeetrid: "))
kytusekulu = liiter/(km/100)
print("Sinu keskmine kütusekulu on: ", kytusekulu)