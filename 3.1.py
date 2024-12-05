fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for ride in fail:
    vastuvõetud.append(int(ride))
print(vastuvõetud)
fail.close()
a=input("Palun sisestage, millise aasta andmeid vajate? ")
print(vastuvõetud [int(a[3])-1])