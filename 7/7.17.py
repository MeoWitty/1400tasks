summa = 0
n = int(input())
for i in range(n):
    a = int(input())
    summa += a
if summa % 2 == 0:
    print("Да")
else:
    print("Нет")