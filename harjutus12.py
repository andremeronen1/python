#15.11.2024 Andre Meronen
#Harjutus 12

pangakonto=15

def konto_haldur(saldo, toiming, summa):
    global pangakonto
    if toiming=="deposiit":
        summa = summa + saldo
         
    else:
        summa = summa - saldo
        pangakonto=summa

        return summa

print(konto_haldur(20,"deposiit", pangakonto))
print(konto_haldur(40,"deposiit", pangakonto))
print(konto_haldur(50,"väljavõte", pangakonto))



















# kytuskulu = lambda x, y: (x/100)*y
# print(kytuskulu(5,150))










# def temperatuur(temp,yhik):
#     """

#     See on maailma parim manual
#     Parameetrid: kui ei tea siis sa loll
#     Näide:google
#     """
#     if yhik=="c":
#         vastus=temp*5/9+32
#     else:
#         vastus=(temp-32)*5/9
#     return round(vastus,2)

# print(temperatuur(3,"c"))
# print(temperatuur(3,"f"))
# print(temperatuur.__doc__)
