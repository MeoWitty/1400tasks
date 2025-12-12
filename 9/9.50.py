n = int(input())
for x in range(1, n):
    a = x
    b = n
    while b != 0:
        a, b = b, a % b
    if a == 1:
        print(x)