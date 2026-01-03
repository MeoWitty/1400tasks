massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
even = [x for x in massiv if x % 2 == 0]
odd = [x for x in massiv if x % 2 != 0]
if even:
    max_even = max(even)
    print(f"Max chetny: {max_even}")
if odd:
    min_odd = min(odd)
    print(f"Min nechetny: {min_odd}")