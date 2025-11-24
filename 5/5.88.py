s = int(input())
count = 0
for i in range(100, 1000):
    sum_cifr = i // 100 + (i // 10) % 10 + i % 10
    if sum_cifr == s:
        count += 1
print(count)