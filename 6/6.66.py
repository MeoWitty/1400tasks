a = int(input())
b = int(input())
c = int(input())

def nod(x, y):
    while y != 0:
        x, y = y, x % y
    return x

result = nod(nod(a, b), c)
print(result)