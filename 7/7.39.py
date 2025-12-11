n = int(input())

# а
sum_abs = 0
for i in range(n):
    a = float(input())
    sum_abs += abs(a)
print(sum_abs)

# б
proizv_abs = 1
spisok = []
for i in range(n):
    a = float(input())
    spisok.append(a)
    proizv_abs *= abs(a)
print(proizv_abs)

# в
summa = 0
znak = 1
for i in range(n):
    a = float(input())
    summa += znak * a
    znak = -znak
print(summa)

# г
summa = 0
znak = 1
temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10
znak = 1 if count % 2 == 1 else -1
temp = n
summa = 0
while temp > 0:
    cifra = temp % 10
    summa += znak * cifra
    znak = -znak
    temp //= 10
print(summa)