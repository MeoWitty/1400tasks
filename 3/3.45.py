k = int(input("Введите k (1-180): "))
p = (k + 1) // 2
n = 9 + p
if k % 2:
    d = n // 10
else:
    d = n % 10
print("Цифра:", d)