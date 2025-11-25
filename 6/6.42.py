n = int(input())

# а
max_cifra = 0
min_cifra = 9
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra > max_cifra:
        max_cifra = cifra
    if cifra < min_cifra:
        min_cifra = cifra
    temp //= 10
print(max_cifra, min_cifra)

# б
print(max_cifra - min_cifra)

# в
print(max_cifra + min_cifra)