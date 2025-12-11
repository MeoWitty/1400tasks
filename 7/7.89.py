n = int(input())
m = int(input())
p = int(input())
count_bolshe_m = 0
for i in range(n):
    a = int(input())
    if a > m:
        count_bolshe_m += 1
if count_bolshe_m % p == 0:
    print("Да")
else:
    print("Нет")