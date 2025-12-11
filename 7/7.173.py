max1 = 0
max2 = 0
for i in range(12):
    skorost = float(input())
    if skorost > max1:
        max2 = max1
        max1 = skorost
    elif skorost > max2:
        max2 = skorost
print(max2)