n = int(input())
count_menwe20 = 0
for i in range(n):
    c = int(input())
    if c < 20:
        count_menwe20 += 1
if count_menwe20 == 5:
    print("Да")
else:
    print("Нет")