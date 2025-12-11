min1 = float('inf')
min2 = float('inf')
for i in range(22):
    vremya = float(input())
    if vremya < min1:
        min2 = min1
        min1 = vremya
    elif vremya < min2:
        min2 = vremya
print(min1, min2)