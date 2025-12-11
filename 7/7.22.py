sum1 = 0
for i in range(8):
    stoimost = float(input())
    sum1 += stoimost

sum2 = 0
for i in range(8):
    stoimost = float(input())
    sum2 += stoimost

if sum1 < sum2:
    print("Первый")
else:
    print("Второй")