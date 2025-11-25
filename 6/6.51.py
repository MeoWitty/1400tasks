n = int(input())
k = int(input())
b = int(input())
x = int(input())
y = int(input())
a = int(input())
m = int(input())
n_val = int(input())

# а
sum_cifr = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    temp //= 10
if sum_cifr > k and n % 2 == 0:
    print("Да")
else:
    print("Нет")

# б
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
if count % 2 == 0 and n <= b:
    print("Да")
else:
    print("Нет")

# в
first = n
while first >= 10:
    first //= 10
last = n % 10
if first == x and last == y:
    print("Да")
else:
    print("Нет")

# г
proizv = 1
temp = n
while temp > 0:
    proizv *= temp % 10
    temp //= 10
if proizv < a and n % b == 0:
    print("Да")
else:
    print("Нет")

# д
sum_cifr = 0
temp = n
while temp > 0:
    sum_cifr += temp % 10
    temp //= 10
if sum_cifr > m and n % n_val == 0:
    print("Да")
else:
    print("Нет")