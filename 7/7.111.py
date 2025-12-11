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
print(sum_malchiki / count_malchiki, sum_devochki / count_devochki)