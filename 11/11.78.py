massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
count_chet = 0
count_okonch_5 = 0
for element in massiv:
    if element % 2 == 0:
        count_chet += 1
    if element % 10 == 5:
        count_okonch_5 += 1
print("Chetnykh:", count_chet)
print("Okonchivayushchikhsya na 5:", count_okonch_5)