#07.01 2024 Andre Meronen
#Harjutus 17
import os

fail=open("palgad.txt")
read=fail.readlines()
mpalgad=[]
npalgad=[]
os.mkdir("palgad")
for i in read:
    r=i.split(",")
    failinimi=r[0] + "_" + r[1]+".txt"
    file=open("palgad/"+failinimi, "a")
    for j in range(1,7):
        file.write(r[j] + "\n")
    if r[3] == "Mees": 
        mpalgad.append(float(r[6]))
    else:
        npalgad.append(float(r[6]))
print(mpalgad)
print(npalgad)


print(sum(mpalgad)/len(mpalgad))
print(sum(npalgad)/len(npalgad))

