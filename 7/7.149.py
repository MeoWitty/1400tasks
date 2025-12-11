n = int(input())
max_massa = 0
min_massa = float('inf')
for i in range(n):
    massa = float(input())
    if massa > max_massa:
        max_massa = massa
    if massa < min_massa:
        min_massa = massa
if max_massa > min_massa * 2:
    print("Да")
else:
    print("Нет")