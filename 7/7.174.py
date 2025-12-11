max1 = 0
max2 = 0
max3 = 0
for i in range(12):
    ochki = int(input())
    if ochki > max1:
        max3 = max2
        max2 = max1
        max1 = ochki
    elif ochki > max2:
        max3 = max2
        max2 = ochki
    elif ochki > max3:
        max3 = ochki
print(max1, max2, max3)