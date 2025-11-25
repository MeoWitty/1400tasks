n = int(input())
temp = n
neubyv = True
pred = 10
while temp > 0:
    tek = temp % 10
    if tek > pred:
        neubyv = False
        break
    pred = tek
    temp //= 10
print(neubyv)