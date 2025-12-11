nomer_para = 0
pred = int(input())
i = 2
while True:
    tek = int(input())
    if tek == 9999:
        break
    if pred % 2 == 0 and tek % 2 == 0:
        nomer_para = i - 1
        break
    pred = tek
    i += 1
if nomer_para > 0:
    print("Да", nomer_para, nomer_para + 1)
else:
    print("Нет")