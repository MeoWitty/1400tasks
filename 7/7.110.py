sum_polnye = 0
count_polnye = 0
sum_ostalnye = 0
count_ostalnye = 0
n = int(input())
for i in range(n):
    massa = float(input())
    if massa > 100:
        sum_polnye += massa
        count_polnye += 1
    else:
        sum_ostalnye += massa
        count_ostalnye += 1
print(sum_polnye / count_polnye, sum_ostalnye / count_ostalnye)