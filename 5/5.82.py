# a
for i in range(10, 100):
    cifra1 = i // 10
    cifra2 = i % 10
    if (cifra1 ** 2 + cifra2 ** 2) % 13 == 0:
        print(i)

# б
for i in range(10, 100):
    sum_cifr = i // 10 + i % 10
    if i == sum_cifr + sum_cifr ** 2:
        print(i)