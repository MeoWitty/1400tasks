count_neprev33 = 0
for i in range(15):
    x = float(input())
    if x <= 33.2:
        count_neprev33 += 1
if count_neprev33 % 4 == 0:
    print("Да")
else:
    print("Нет")