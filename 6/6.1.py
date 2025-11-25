a = int(input())
b = int(input())

# a
celoe = 0
temp = a
while temp >= b:
    temp -= b
    celoe += 1
print(celoe)

# б
ost = a
while ost >= b:
    ost -= b
print(ost)