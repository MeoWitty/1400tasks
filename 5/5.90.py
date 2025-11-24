n = int(input())
a, b = 1, 1
summa = 2
for i in range(3, n + 1):
    a, b = b, a + b
    summa += b
if summa % 2 == 0:
    print("Да")
else:
    print("Нет")