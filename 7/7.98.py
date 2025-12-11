n = int(input())
nomer_para = 0
pred = int(input())
for i in range(2, n + 1):
    tek = int(input())
    if pred % 2 != 0 and tek % 2 != 0:
        nomer_para = i - 1
        break
    pred = tek
if nomer_para > 0:
    print("Да", nomer_para, nomer_para + 1)
else:
    print("Нет")