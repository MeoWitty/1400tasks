for n in range(300, 601):
    sum_del = 0
    for i in range(1, n):
        if n % i == 0:
            sum_del += i
    if sum_del % 10 == 0:
        print(n)