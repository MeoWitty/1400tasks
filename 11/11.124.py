massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
even_elements = [x for x in massiv if x % 2 == 0]
odd_elements = [x for x in massiv if x % 2 != 0]
if even_elements:
    max_even = max(even_elements)
    print(f"Maximum chetnykh: {max_even}")
if odd_elements:
    min_odd = min(odd_elements)
    print(f"Minimum nechetnykh: {min_odd}")