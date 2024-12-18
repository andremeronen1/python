#18.12.2024 Andre Meronen
#Harjutus 10
#kaugushüpe

tulemus1=int(input("esimene tulemus: "))
tulemus2=int(input("teine tulemus: "))
tulemus3=int(input("kolmas tulemus: "))
tulemused=tulemus1,tulemus2,tulemus3
parim=max(tulemused)
keskmine=round(sum(tulemused)/len(tulemused))
print(f"parim tulemus on {parim}")
print(f"keskmine tulemus on {keskmine}")
