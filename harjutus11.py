#08.11.2024 Andre Meronen
#Harjutus 11

def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikim sõna on {pikim} märki!")

pikim_sona("üks", "kaks", "kolkümmend")