massiv = [5, 4, 3, 4, 5, 4, 3, 4, 5, 4]
count_4 = 0
count_5 = 0
for element in massiv:
    if element == 4:
        count_4 += 1
    elif element == 5:
        count_5 += 1
print("Chetverok:", count_4)
print("Pyaterok:", count_5)