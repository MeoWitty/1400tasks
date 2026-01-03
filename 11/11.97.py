massiv = [150, 160, 170, 165, 155, 175, 180, 172, 168, 162, 158, 152, 148, 145, 140, 135, 130, 125, 120, 115, 110, 105, 150, 160, 170]
sredniy_rost = sum(massiv) / len(massiv)
count = 0
for element in massiv:
    if element > sredniy_rost:
        count += 1
print(count)