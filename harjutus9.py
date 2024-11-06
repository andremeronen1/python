# 24.10.24 Andre Meronen
# Ülesanne 9 tsüklid
import random
import turtle
#9.14 harjutus 3 kujundit















"""
ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

kolmsada = []
labisoit = []
hinnad = []
for car in ev_data:    
    for i in car:
        print(f"{i:30}", end=" ")
    if car[1] != "range" or car[2] != "price":
        labisoit.append(int(car[1]))
        if int(car[1])>=300:
            kolmsada.append(car[0])
        hinnad.append(int(car[2]))
        print(int(car[2])/int(car[1]))
    else:
        print("ratio")
print(f"keskmine läbisoit: {sum(labisoit)/len(labisoit)}")
print(f"keskmine hind: {sum(hinnad)/len(hinnad)}€")
print(kolmsada)
"""


"""
summa = 0 
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]

for i in even_nums:
    if i%2==0:
        summa+=i
    else:
        break

print(summa)
"""







"""
for i in range(1,6):
    print("*" * i)
print()
for i in range(1,6):
    print("*" * (6-i))
print()
for i in range(1,6):
    print(" "*(5-i)+"*" * i)
print()
for i in range(1,6):
    print(" "*(-1+i)+"*"*(6-i))
"""









"""
for i in range(11):
    print(f"{i} x {i} = {i*i}")


tehted = ["+","-","*","/",]

for i in range(6):
    j = random.randint(1,10)
    k = random.randint(1,10)
    tehe = random.choice(tehted)
    if tehe=="+":
        print(f"{j} {tehe} {k} = {j+k}")
        vastus = int(input("Vastus: "))
        if vastus==j+k:
            print("õige")
            punktid+=1
        else:
            print("vale")
    elif tehe=="-":
        vastus = int(input("Vastus: "))
        if vastus==j-k:
            print(f"{j} {tehe} {k} = {j-k}")
            print("õige")
            punktid+= 1
        else:
            print("vale")

    elif tehe=="*":
        vastus = int(input("Vastus: "))
        if vastus==j*k:
            print("õige")
            punktid+=1
        else:
            print("vale")
        if vastus==j/k:
            print(f"{j} {tehe} {k} = {j/k}")
    print(str(punktid/kysimuste_arv)*100)+"%"
    if punkt/kysimuste_arv=0,5:
        print("Vale")
    """







# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# meeles = []



# for opilane in ryhma_hinded:
#     meeles.append(float(opilane.split(" ")[1]))

# print(f"Parim tulemus {max(meeles)}")
# print(f"Halvim tulemus {min(meeles)}")
# print(f"Keskmine tulemus {round(sum(meeles)/len(meeles),2)}")





# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# unimed = []


# for nimi in nimed:
#     if nimi not in unimed:
#         unimed.append(nimi)
# print(unimed)

# for i in range(1,21):
#      print(i, end=" ")
# print()



#for i in range(1,21):
#    print(random.randint(14, 99), end=" ")
#print()


#loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# paaris = []
# # # paaritud = []

# # # for i in loend:
# # #     if i%2==0:
# # #         paaris.append(i)
# # #     else:
# # #         paaritud.append(i)

# # # print(f"Paaris arvude summa on: {sum(paaris)}")
# # # print(f"Paaritute arvude summa on: {sum(paaritud)}")

# # # print()




# # # for i in range(1,43):
# # #     if i%3==0:
# # #         print(i,"TIKTAK", end=" ")
# # #     elif i%3==0:
# # #         print(i,"TIK", end=" ")
# # #     elif i%5==0:
# # #         print(i,"TAK", end=" ")
# # #     else:
# # #         print(i, end=" ")

# # # print()
turtle.done