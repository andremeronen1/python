#14.01.2024 Andre Meronen
#harjutus 19

import json
klass12=0
with open ("haridustulemused.json","r",encoding="utf-8") as file:
   
    opilased=json.load(file)
    for opilane in opilased:
        if opilane["klass"]=="12":
            klass12+=1
            print(opilane["nimi"])
            for trenn in opilane["tegevused"]:
                print(trenn)
            print("----------------")

print(f"12.klassis õpib {klass12} õpilast")