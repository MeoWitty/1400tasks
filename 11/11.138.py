massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
negative = [x for x in massiv if x < 0]
if negative:
    max_negative = max(negative)
    print(f"Maksimalnoe otritsatelnoe: {max_negative}")