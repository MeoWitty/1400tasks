for a in range(1, 50000):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    b = sum_a
    if b < 50000 and b != a:
        sum_b = 0
        for i in range(1, b):
            if b % i == 0:
                sum_b += i
        if sum_b == a and a < b:
            print(a, b)