fail=open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida):
        print(rida)