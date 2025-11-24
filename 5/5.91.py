n = int(input())

# a
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# б
sum_del = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_del += i
print(sum_del)

# в
sum_chet = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        sum_chet += i
print(sum_chet)

# г
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)

# д
count_nechet = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 != 0:
        count_nechet += 1
print(count_nechet)

# е
count_chet = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        count_chet += 1
print(count_chet)

# ж
d = int(input())
count_bolshe = 0
for i in range(1, n + 1):
    if n % i == 0 and i > d:
        count_bolshe += 1
print(count_bolshe)