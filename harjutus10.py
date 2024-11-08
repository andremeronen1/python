#08.11.2024 Andre Meronen
#Harjutus 10
import random

#Arvu äraarvamise mäng
katsed = []
loop = 1
arvamused = 0
suv = random.randint(1,10)
print(suv)

while loop==1:
    arva=int(input("Arva arv 1-10: "))
    arvamused+=1
    if arva == suv:
        print("õige")
        print(f"Proovisid arvata {arvamused} korda!")
        katsed.append(arvamused)
        uuesti = input("Soovid uuesti? (j/e): ")
        if uuesti=="j":
            suv = random.randint(1,10)
            arvamused = 0
        else:
            break
    else: 
        print("Vale")
print("Game Over")
print(katsed)



#arvude keskmine
# arvud = []
# loop = 1

# while loop==1:
#     arv = input("Lisa arv: ")
#     if arv=="":
#         break
#     arvud.append(int(arv))


# print(sum(arvud)/len(arvud))




