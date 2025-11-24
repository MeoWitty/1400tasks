a, b = 1, 1
for i in range(3, 11):
    a, b = b, a + b
    print(b)