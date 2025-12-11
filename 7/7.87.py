n = int(input())
count_polozh = 0
for i in range(n):
    a = int(input())
    if a > 0:
        count_polozh += 1
if count_polozh % 3 == 0:
    print("Да")
else:
    print("Нет")