massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
negative = [x for x in massiv if x < 0]
positive = [x for x in massiv if x > 0]
if negative:
    min_negative = min(negative)
    print(f"Min otritsatelny: {min_negative}")
if positive:
    max_positive = max(positive)
    print(f"Max polozhitelny: {max_positive}")