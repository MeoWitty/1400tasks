n = int(input())
for i in range(10, 100):
    if i % n == 0 or i // 10 == n or i % 10 == n:
        print(i)