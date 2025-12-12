n = int(input())
m = int(input())
for x in range(1, n):
    a = x
    b = m
    while b != 0:
        a, b = b, a % b
    if a == 1:
        print(x)