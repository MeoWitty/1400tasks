n = int(input())
a, b = 1, 1
while b < n:
    a, b = b, a + b
if b == n:
    print("Да")
else:
    print("Нет")