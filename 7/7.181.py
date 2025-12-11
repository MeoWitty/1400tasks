# а
pravilno = True
for i in range(20):
    chislo = int(input())
    if chislo % 10 > 6 or chislo // 10 > 6:
        pravilno = False
        break
print(pravilno)

# б
pravilno = True
for i in range(20):
    chislo = int(input())
    pervaya = chislo // 10
    vtoraya = chislo % 10
    if pervaya > 6 or vtoraya > 6 or pervaya < 0 or vtoraya < 0:
        pravilno = False
        break
print(pravilno)