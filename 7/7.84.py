count_polozh = 0
for i in range(10):
    a = int(input())
    if a > 0:
        count_polozh += 1
if count_polozh <= 5:
    print("Да")
else:
    print("Нет")