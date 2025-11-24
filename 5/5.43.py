n = int(input())
a = 1
print(a)
for k in range(1, n + 1):
    a = k * a + 1 / k
    print(a)