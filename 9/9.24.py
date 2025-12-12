# а
a = int(input())
b = int(input())
max_count = 0
max_n = a
for n in range(a, b + 1):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count > max_count:
        max_count = count
        max_n = n
print(max_n)

# б
a = int(input())
b = int(input())
max_count = 0
min_n = b
for n in range(a, b + 1):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count > max_count:
        max_count = count
        min_n = n
    elif count == max_count and n < min_n:
        min_n = n
print(min_n)