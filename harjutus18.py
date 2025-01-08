#08.01.2024 Andre Meronen
#harjutus 18
import csv 
faili_nimi="EstonianBasketballGames.csv"
meeskonnad={}
with open(faili_nimi, mode="r", encoding="utf-8") as fail:
    csv_lugeja = csv.reader(fail)
    for rida in csv_lugeja:
        print(rida[1])