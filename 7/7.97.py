nomer_para = 0
pred = int(input())
i = 2
while True:
    tek = int(input())
    if tek == -1:
        break
    if tek == pred:
        nomer_para = i - 1
        break
    pred = tek
    i += 1
if nomer_para > 0:
    print("Да", nomer_para, nomer_para + 1)
else:
    print("Нет")