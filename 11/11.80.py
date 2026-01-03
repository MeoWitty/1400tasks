massiv = [5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4, 3, 2, 5, 4]
count_5 = 0
count_4 = 0
count_3 = 0
count_2 = 0
for element in massiv:
    if element == 5:
        count_5 += 1
    elif element == 4:
        count_4 += 1
    elif element == 3:
        count_3 += 1
    elif element == 2:
        count_2 += 1
print("Pyaterok:", count_5)
print("Chetverok:", count_4)
print("Troek:", count_3)
print("Dvoek:", count_2)