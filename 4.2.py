def mahlapakkide_arv(kg):
    arv = int(round(kg*0.4/3,0))
    return arv

ounad = int(input("Õunte kogus: "))
print(mahlapakkide_arv(ounad))