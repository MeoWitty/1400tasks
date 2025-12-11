summa = 0
count = 0
while True:
    a = int(input())
    if a % 2 == 0:
        break
    summa += a
    count += 1
print(summa, count)