sum_malchiki = 0
count_malchiki = 0
sum_devochki = 0
count_devochki = 0
n = int(input())
for i in range(n):
    rost = float(input())
    if rost < 0:
        sum_malchiki += abs(rost)
        count_malchiki += 1
    else:
        sum_devochki += rost
        count_devochki += 1

sred_malchiki = sum_malchiki / count_malchiki
sred_devochki = sum_devochki / count_devochki

if sred_malchiki > sred_devochki + 10:
    print("Да")
else:
    print("Нет")