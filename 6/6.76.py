a = int(input())
b = int(input())
dlina = 0
while a > 0 and b > 0:
    if a >= b:
        dlina += a
        a -= 1
    else:
        dlina += b
        b -= 1
print(dlina)