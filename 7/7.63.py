count_pyaterok = 0
count_dvoek = 0
n = int(input())
for i in range(n):
    ocenka = int(input())
    if ocenka == 5:
        count_pyaterok += 1
    elif ocenka == 2:
        count_dvoek += 1
print(count_pyaterok, count_dvoek)