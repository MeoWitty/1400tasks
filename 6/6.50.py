n = int(input())
a = int(input())
b = int(input())
k = int(input())
m = int(input())

# а
sum_cifr = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    temp //= 10
if sum_cifr < a:
    print("Да")
else:
    print("Нет")

# б
proizv = 1
temp = n
while temp > 0:
    proizv *= temp % 10
    temp //= 10
if proizv > b:
    print("Да")
else:
    print("Нет")

# в
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
if count == k:
    print("Да")
else:
    print("Нет")

# г
temp = n
while temp >= 10:
    temp //= 10
if temp > m:
    print("Да")
else:
    print("Нет")