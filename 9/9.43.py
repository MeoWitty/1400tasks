a = int(input())
b = int(input())
c = int(input())
while b != 0:
    a, b = b, a % b
while c != 0:
    a, c = c, a % c
print(a)