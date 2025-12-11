sum_avto = 0
count_avto = 0
sum_moto = 0
count_moto = 0

n = int(input())
for i in range(n):
    tip = input()
    stoimost = float(input())
    if tip == "авто":
        sum_avto += stoimost
        count_avto += 1
    else:
        sum_moto += stoimost
        count_moto += 1

sred_avto = sum_avto / count_avto
sred_moto = sum_moto / count_moto

if sred_avto > sred_moto * 3:
    print("Да")
else:
    print("Нет")