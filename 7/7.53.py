n = int(input())

# а
sum_menwe25 = 0
for i in range(n):
    m = int(input())
    if m < 25:
        sum_menwe25 += m
if sum_menwe25 <= 50:
    print("Да")
else:
    print("Нет")

# б
sum_neprev20 = 0
for i in range(n):
    m = int(input())
    if m <= 20:
        sum_neprev20 += m
if sum_neprev20 % 3 == 0:
    print("Да")
else:
    print("Нет")