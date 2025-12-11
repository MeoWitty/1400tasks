sum_bolshe10 = 0
count_bolshe10 = 0
n = int(input())
for i in range(n):
    b = float(input())
    if b > 10:
        sum_bolshe10 += b
        count_bolshe10 += 1
if count_bolshe10 > 0:
    print(sum_bolshe10 / count_bolshe10)
else:
    print("Нет таких")