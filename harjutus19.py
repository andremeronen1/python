#14.01.2024 Andre Meronen
#harjutus 19

import json
klass12=0
with open ("haridustulemused.json","r",encoding="utf-8") as file:
    opilased=json.load(file)
    for opilased in opilased:
        klass=["number"]