min1 = float('inf')
min2 = float('inf')
den1 = 0
den2 = 0
for den in range(1, 366):
    temp = float(input())
    if temp < min1:
        min2 = min1
        den2 = den1
        min1 = temp
        den1 = den
    elif temp < min2:
        min2 = temp
        den2 = den
print(den1, den2)