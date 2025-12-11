n = int(input())

# а
sum_bolshe20 = 0
for i in range(n):
    b = int(input())
    if b > 20:
        sum_bolshe20 += b
if sum_bolshe20 > 100:
    print("Да")
else:
    print("Нет")

# б
sum_menwe50 = 0
for i in range(n):
    b = int(input())
    if b < 50:
        sum_menwe50 += b
if sum_menwe50 % 2 == 0:
    print("Да")
else:
    print("Нет")