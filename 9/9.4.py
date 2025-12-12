# 1)
s = 0
for uchenik in range(12):
    a = int(input())
    b = int(input())
    c = int(input())
    s += a + b + c
print(s)

# 2)
s = 0
for predmet in range(3):
    for uchenik in range(12):
        o = int(input())
        s += o
print(s)