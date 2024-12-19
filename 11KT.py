#18.12.2024 Andre Meronen
#harjutus 11
#salakeel

#küsib kasutajalt kas soovid salakeelt luua või salakeelt tõlkida
salakeele_valik=input("1=soovid salakeelt luua, 2=soovid salakeelt tõlkida ")
#kui sisestad 1 siis hakkab looma 
if salakeele_valik=="1":
    salakeel=input("Sisesta sõna: ")
    print(salakeel.replace("s","5"))
#kui sisestad 2 siis hakkab tõlkima
elif salakeele_valik=="2":
    salakeel=input("Sisesta sõna: ")
    print(salakeel.replace("5","s"))
