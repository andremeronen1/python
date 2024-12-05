import random
ounu=14
poisse=int(input("Mitu pöialpoissi tahab õunu? "))
for i in range(poisse):
    ounu -= random.randint(1,2)
print(ounu)