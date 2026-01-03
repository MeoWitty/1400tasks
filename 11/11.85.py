massiv = [150, 160, 170, 165, 155, 175, 180, 172, 168, 162, 158, 152, 148, 145, 140, 135, 130, 125, 120, 115, 110, 105, 150, 160, 170, 165, 155, 175, 180, 172]
count_bolshe170 = 0
for element in massiv:
    if element > 170:
        count_bolshe170 += 1
print("Bolshe 170 cm:", count_bolshe170)
if count_bolshe170 >= 5:
    print("Mozhno sobrat komandu")
else:
    print("Nelzya sobrat komandu")