n = int(input())
b = int(input())
summa = 0
for i in range(n):
    x = int(input())
    summa += x
if summa % b == 0:
    print("Да")
else:
    print("Нет")