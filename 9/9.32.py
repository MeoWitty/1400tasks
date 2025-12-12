a = int(input())
b = int(input())
max_sum = 0
max_n = a
for n in range(a, b + 1):
    sum_del = 0
    for i in range(1, n):
        if n % i == 0:
            sum_del += i
    if sum_del > max_sum:
        max_sum = sum_del
        max_n = n
print(max_n)