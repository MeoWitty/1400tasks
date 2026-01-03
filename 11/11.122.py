massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
negative_elements = [x for x in massiv if x < 0]
if negative_elements:
    max_negative = max(negative_elements)
    print(max_negative)
else:
    print("Net otritsatelnykh elementov")