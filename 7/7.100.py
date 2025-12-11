n = int(input())
vozrast = True
nomer_narusheniya = 0
pred = float(input())
for i in range(2, n + 1):
    tek = float(input())
    if tek < pred:
        vozrast = False
        nomer_narusheniya = i
        break
    pred = tek
if vozrast:
    print("Да")
else:
    print("Нет", nomer_narusheniya)