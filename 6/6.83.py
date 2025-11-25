n = int(input())
temp = n
cifry = []
while temp > 0:
    cifry.append(temp % 10)
    temp //= 10
cifry.reverse()

vozrast = True
for i in range(len(cifry) - 1):
    if cifry[i] >= cifry[i + 1]:
        vozrast = False
        break

ubyv = True
for i in range(len(cifry) - 1):
    if cifry[i] <= cifry[i + 1]:
        ubyv = False
        break

print(vozrast or ubyv)