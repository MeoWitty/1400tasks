massiv = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]
count_3 = 0
count_2 = 0
count_1 = 0
for element in massiv:
    if element == 3:
        count_3 += 1
    elif element == 2:
        count_2 += 1
    elif element == 1:
        count_1 += 1
print("Vyigryshey:", count_3)
print("Nichikh:", count_1)
print("Proigryshey:", count_2)