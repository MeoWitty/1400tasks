massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
negative_elements = [x for x in massiv if x < 0]
positive_elements = [x for x in massiv if x > 0]
if negative_elements:
    min_negative = min(negative_elements)
    print(f"Minimum otritsatelnykh: {min_negative}")
if positive_elements:
    max_positive = max(positive_elements)
    print(f"Maximum polozhitelnykh: {max_positive}")