n = int(input())

# а
summa = 0
for i in range(n):
    a = int(input())
    summa += a ** 2
print(summa)

# б
raznost = 0
znak = 1
for i in range(n):
    a = int(input())
    raznost += znak * a ** 2
    znak = -znak
print(raznost)