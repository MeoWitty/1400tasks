count_5 = 0
count_4 = 0
count_3 = 0
count_2 = 0
n = int(input())
for i in range(n):
    ocenka = int(input())
    if ocenka == 5:
        count_5 += 1
    elif ocenka == 4:
        count_4 += 1
    elif ocenka == 3:
        count_3 += 1
    elif ocenka == 2:
        count_2 += 1
print(count_5, count_4, count_3, count_2)