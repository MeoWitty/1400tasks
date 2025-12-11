n = int(input())
p = float(input())
sum_bolshe20 = 0
for i in range(n):
    d = float(input())
    if d > 20.5:
        sum_bolshe20 += d
if sum_bolshe20 < p:
    print("Да")
else:
    print("Нет")