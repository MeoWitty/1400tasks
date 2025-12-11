min_vremya = float('inf')
while True:
    vremya = float(input())
    if vremya == 0:
        break
    if vremya < min_vremya:
        min_vremya = vremya
    print(min_vremya)