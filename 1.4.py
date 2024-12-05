inimeste_arv = int(input("Sisesta inimeste arv: "))
kohtade_arv = int(input("Sisesta kohtade arv: "))
busside_arv = inimeste_arv//kohtade_arv
viimases_bussis = inimeste_arv%kohtade_arv

if viimases_bussis >0:
    busside_arv=+1
print(f"busse on vaja: {busside_arv}")
print(f"viimases bussis on {viimases_bussis} inimest")

