summa = 0
while True:
    stoimost = float(input())
    if stoimost == 0:
        break
    if stoimost > 1000:
        summa += stoimost
print(summa)