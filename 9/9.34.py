# а)
n = int(input())
count = 0
for k10 in range(n // 10 + 1):
    for k5 in range((n - k10 * 10) // 5 + 1):
        for k2 in range((n - k10 * 10 - k5 * 5) // 2 + 1):
            k1 = n - k10 * 10 - k5 * 5 - k2 * 2
            if k1 >= 0:
                count += 1
print(count)

# б)
n = int(input())
for k10 in range(n // 10 + 1):
    for k5 in range((n - k10 * 10) // 5 + 1):
        for k2 in range((n - k10 * 10 - k5 * 5) // 2 + 1):
            k1 = n - k10 * 10 - k5 * 5 - k2 * 2
            if k1 >= 0:
                print(k10, k5, k2, k1)