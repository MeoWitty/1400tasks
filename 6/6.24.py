n = int(input())

# а
summa = 0
znak = 1
while n > 0:
    summa += znak * (n % 10)
    znak = -znak
    n //= 10
print(summa)

# б
summa = 0
znak = 1
temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10
znak = 1 if count % 2 == 1 else -1
while n > 0:
    summa += znak * (n % 10)
    znak = -znak
    n //= 10
print(summa)