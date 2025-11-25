n = int(input())
p = int(input())
summa = 0
for i in range(n):
    b = int(input())
    summa += b
if summa < p:
    print("Да")
else:
    print("Нет")