n = int(input())

# а
sum_cifr = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    temp //= 10
print(sum_cifr)

# б
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
print(count)

# в
proizv = 1
temp = n
while temp > 0:
    proizv *= temp % 10
    temp //= 10
print(proizv)

# г
sum_cifr = 0
count = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    count += 1
    temp //= 10
print(sum_cifr / count)

# д
sum_kv = 0
temp = n
while temp > 0:
    sum_kv += (temp % 10) ** 2
    temp //= 10
print(sum_kv)

# е
sum_kub = 0
temp = n
while temp > 0:
    sum_kub += (temp % 10) ** 3
    temp //= 10
print(sum_kub)

# ж
temp = n
while temp >= 10:
    temp //= 10
print(temp)

# з
last = n % 10
temp = n
while temp >= 10:
    temp //= 10
first = temp
print(first + last)