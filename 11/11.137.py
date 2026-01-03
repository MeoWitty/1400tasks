massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
positive = [x for x in massiv if x > 0]
if positive:
    min_positive = min(positive)
    print(f"Minimalnoe polozhitelnoe: {min_positive}")