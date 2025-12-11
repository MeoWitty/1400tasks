n = int(input())
max_chislo = float('-inf')
min_chislo = float('inf')
for i in range(n):
    a = int(input())
    if a > max_chislo:
        max_chislo = a
    if a < min_chislo:
        min_chislo = a
if max_chislo - min_chislo <= 25:
    print("Да")
else:
    print("Нет")