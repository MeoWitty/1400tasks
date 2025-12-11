# 1 вариант (с повторным вводом)
n = int(input())
max_dlina = 1
tek_dlina = 1
pred = int(input())
for i in range(n-1):
    tek = int(input())
    if (tek > pred and tek_dlina > 0) or (tek < pred and tek_dlina < 0):
        if (tek > pred and tek_dlina > 0) or (tek < pred and tek_dlina < 0):
            if tek_dlina > 0 and tek > pred:
                tek_dlina += 1
            elif tek_dlina < 0 and tek < pred:
                tek_dlina -= 1
            else:
                if abs(tek_dlina) > max_dlina:
                    max_dlina = abs(tek_dlina)
                if tek > pred:
                    tek_dlina = 2
                else:
                    tek_dlina = -2
    else:
        if abs(tek_dlina) > max_dlina:
            max_dlina = abs(tek_dlina)
        if tek > pred:
            tek_dlina = 2
        else:
            tek_dlina = -2
    pred = tek
if abs(tek_dlina) > max_dlina:
    max_dlina = abs(tek_dlina)
print(max_dlina)

# 2 вариант (с однократным вводом)
spisok = []
while True:
    chislo = int(input())
    if chislo == 10000:
        break
    spisok.append(chislo)

max_dlina = 1
tek_dlina = 1
for i in range(1, len(spisok)):
    if spisok[i] > spisok[i-1] and tek_dlina > 0:
        tek_dlina += 1
    elif spisok[i] < spisok[i-1] and tek_dlina < 0:
        tek_dlina -= 1
    else:
        if abs(tek_dlina) > max_dlina:
            max_dlina = abs(tek_dlina)
        if spisok[i] > spisok[i-1]:
            tek_dlina = 2
        else:
            tek_dlina = -2
if abs(tek_dlina) > max_dlina:
    max_dlina = abs(tek_dlina)
print(max_dlina)