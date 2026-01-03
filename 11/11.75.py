massiv = [3, 0, 1, 3, 1, 0, 3, 0, 1, 3, 1, 0, 3, 0, 1, 3, 1, 0, 3, 0]
count_3 = 0
count_0 = 0
for element in massiv:
    if element == 3:
        count_3 += 1
    elif element == 0:
        count_0 += 1
print("Vyigryshey:", count_3)
print("Proigryshey:", count_0)