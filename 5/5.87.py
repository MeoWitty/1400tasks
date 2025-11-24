count = 0
for i in range(100, 501):
    sum_cifr = i // 100 + (i // 10) % 10 + i % 10
    if sum_cifr == 15:
        count += 1
print(count)