for n in range(50, 71):
    sum_del = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_del += i
    print(n, sum_del)