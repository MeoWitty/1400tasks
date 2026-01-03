massiv = [5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6, 0, 9, 0, 1, 0, 5, 0, 3, 0, 7, 0, 2, 0, 8, 0, 4, 0, 6]
count_0 = 0
for element in massiv:
    if element == 0:
        count_0 += 1
if count_0 == 10:
    print("Verno")
else:
    print("Ne verno")