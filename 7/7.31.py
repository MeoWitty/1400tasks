summa = 0
count = 0
while True:
    num = int(input())
    if num < 0:
        break
    summa += num
    count += 1
print(summa / count)