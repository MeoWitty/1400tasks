n = int(input())
m = int(input())
sum_bolshe_m = 0
count_bolshe_m = 0
for i in range(n):
    a = int(input())
    if a > m:
        sum_bolshe_m += a
        count_bolshe_m += 1
if count_bolshe_m > 0:
    print(sum_bolshe_m / count_bolshe_m)
else:
    print("Нет таких")