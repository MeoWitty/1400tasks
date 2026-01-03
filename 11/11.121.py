massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
positive_elements = [x for x in massiv if x > 0]
if positive_elements:
    min_positive = min(positive_elements)
    print(min_positive)
else:
    print("Net polozhitelnykh elementov")