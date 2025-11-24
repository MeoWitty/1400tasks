# a
for i in range(100, 1000):
    if i == (i ** 2) % 1000:
        print(i)

# б
for i in range(100, 1000):
    sum_cifr = i // 100 + (i // 10) % 10 + i % 10
    if i % 7 == 0 and sum_cifr % 7 == 0:
        print(i)