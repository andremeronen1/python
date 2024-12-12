def tervitus(n):
    for i in range (n):
        print('Võõrustaja: "Tere!"')
        print(f"Täna {i+1}. kord tervitada, mõtiskleb võõrustaja")
        print('Külaine: "Tere!"')
s=int(input("Külaliste arv: "))
tervitus(s)