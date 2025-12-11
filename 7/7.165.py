max_srednyaya_skorost = 0
nomer_avto = 0
for i in range(1, 26):
    rasstoyanie = float(input())
    vremya = float(input())
    srednyaya_skorost = rasstoyanie / vremya
    if srednyaya_skorost > max_srednyaya_skorost:
        max_srednyaya_skorost = srednyaya_skorost
        nomer_avto = i
print(nomer_avto)