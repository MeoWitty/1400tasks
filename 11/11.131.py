massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
if massiv:
    max_element = max(massiv)
    min_element = min(massiv)
    index_max = massiv.index(max_element)
    index_min = massiv.index(min_element)
    print(f"Nomer maksimuma: {index_max}")
    print(f"Nomer minimuma: {index_min}")