ringide_arv=6
i = 1
porgandite_koguarv=0
while i <=ringide_arv:
    if i%2==0:
        porgandite_koguarv+=1
        print(i)
    i+=1

print(f"porgandite koguarv on: {porgandite_koguarv}")