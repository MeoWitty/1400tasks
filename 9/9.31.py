n = 2
while n < 100000:
    sum_del = 0
    for i in range(1, n):
        if n % i == 0:
            sum_del += i
    if sum_del == n:
        print(n)
    n += 1