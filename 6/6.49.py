n = int(input())

# а
sum_cifr = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    temp //= 10
if sum_cifr > 10:
    print("Да")
else:
    print("Нет")

# б
proizv = 1
temp = n
while temp > 0:
    proizv *= temp % 10
    temp //= 10
if proizv < 50:
    print("Да")
else:
    print("Нет")

# в
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
if count % 2 == 0:
    print("Да")
else:
    print("Нет")

# г
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
if count == 4:
    print("Да")
else:
    print("Нет")

# д
temp = n
while temp >= 10:
    temp //= 10
if temp <= 6:
    print("Да")
else:
    print("Нет")

# е
last = n % 10
temp = n
while temp >= 10:
    temp //= 10
first = temp
if first == last:
    print("Да")
else:
    print("Нет")

# ж
last = n % 10
temp = n
while temp >= 10:
    temp //= 10
first = temp
if first > last:
    print("Первая")
else:
    print("Последняя")