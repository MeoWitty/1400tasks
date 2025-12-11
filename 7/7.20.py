gruzopodem = float(input())
summa = 0
n = int(input())
for i in range(n):
    massa = float(input())
    summa += massa
if summa > gruzopodem:
    print("Превышает")
else:
    print("Не превышает")