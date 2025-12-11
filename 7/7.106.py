summa = 0
count = 0
for i in range(15):
    c = float(input())
    if c > 20:
        summa += c
        count += 1
print(summa / count)