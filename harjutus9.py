#24.10.24 Andre Meronen
#Ülesanne 9 tsüklid
import random



for i in range(1,21):
    print(i, end=" ")
print()



for i in range(1,21):
    print(random.randint(14, 99), end=" ")
print()


loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []

for i in loend:
    if i%2==0:
        paaris.append(i)
    else:
        paaritud.append(i)

print(f"Paaris arvude summa on: {sum(paaris)}")
print(f"Paaritute arvude summa on: {sum(paaritud)}")

print()




for i in range(1,43):
    if i%3==0:
        print(i,"TIKTAK", end=" ")
    elif i%3==0:
        print(i,"TIK", end=" ")
    elif i%5==0:
        print(i,"TAK", end=" ")
    else:
        print(i, end=" ")

print()