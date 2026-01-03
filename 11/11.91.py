massiv = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320]
summa_poln = 0
count_poln = 0
summa_ost = 0
count_ost = 0
for element in massiv:
    if element > 100:
        summa_poln += element
        count_poln += 1
    else:
        summa_ost += element
        count_ost += 1
if count_poln > 0:
    print("Srednee massy polnykh:", summa_poln / count_poln)
if count_ost > 0:
    print("Srednee massy ostalnykh:", summa_ost / count_ost)