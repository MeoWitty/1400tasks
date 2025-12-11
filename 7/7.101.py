vozrast = True
nomer_narusheniya = 0
pred = float(input())
i = 2
while True:
    tek = float(input())
    if tek == 10000:
        break
    if tek < pred:
        vozrast = False
        nomer_narusheniya = i
        break
    pred = tek
    i += 1
if vozrast:
    print("Да")
else:
    print("Нет", nomer_narusheniya)