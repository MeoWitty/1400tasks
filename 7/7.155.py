max_dlina = 1
tek_dlina = 1
pred = int(input())
while True:
    tek = int(input())
    if tek == 10000:
        break
    if tek > pred:
        tek_dlina += 1
        if tek_dlina > max_dlina:
            max_dlina = tek_dlina
    else:
        tek_dlina = 1
    pred = tek
print(max_dlina)