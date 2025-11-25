n = int(input())

# а
obratnoe = 0
temp = n
while temp > 0:
    obratnoe = obratnoe * 10 + temp % 10
    temp //= 10
print(obratnoe)

# б
dlina = 0
temp = n
while temp > 0:
    dlina += 1
    temp //= 10
result = 2 * (10 ** (dlina + 1)) + n * 10 + 2
print(result)

# в
a = int(input())
result = 0
step = 1
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra != a:
        result = cifra * step + result
        step *= 10
    temp //= 10
print(result)

# г
last = n % 10
temp = n
count = 0
while temp >= 10:
    count += 1
    temp //= 10
first = temp
sred = n % (10 ** count) // 10
result = last * (10 ** count) + sred * 10 + first
print(result)

# д
temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10
result = n * (10 ** count) + n
print(result)