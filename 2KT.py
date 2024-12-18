#18.12.2024 Andre Meronen
#Harjutus 2
#vanused

vanused=2,28,56,53,48,60,26,35,97,68,5,77,7,1,41,76,11,32,45,65,95,44,66,54,89,73,51,58,40,82,78,14,88,80,83,61,49,46,38,33,100,10,50,64,12,37,29,74,52,27
vanim=max(vanused)
noorim=min(vanused)
kogusumma=sum(vanused)
keskmine=round(kogusumma/len(vanused))
print(f"Kõige vanim on {vanim}")
print(f"Kõige noorim on {noorim}")
print(f"Kogusumma on {kogusumma}")
print(f"Keskmine vanus on {keskmine}")
