massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
if massiv:
    max_element = max(massiv)
    min_element = min(massiv)
    index_max = massiv.index(max_element)
    index_min = massiv.index(min_element)
    if index_max < index_min:
        print("Maximum ranbshe")
    else:
        print("Minimum ranbshe")