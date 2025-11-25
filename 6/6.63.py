n = int(input())
obratnoe = 0
temp = n
while temp > 0:
    obratnoe = obratnoe * 10 + temp % 10
    temp //= 10
if n == obratnoe:
    print("Да")
else:
    print("Нет")