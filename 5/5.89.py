count = 0
for i in range(100, 1000):
    sum_cifr = i // 100 + (i // 10) % 10 + i % 10
    if i % 7 == 0 and sum_cifr % 7 == 0:
        count += 1
print(count)