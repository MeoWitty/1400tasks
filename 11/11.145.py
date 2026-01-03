massiv = [5, -3, 10, -7, 0, 15, -2, 8, -1, 12]
if massiv:
    max_abs_element = max(massiv, key=abs)
    index_max_abs = massiv.index(max_abs_element)
    print(f"Maximum po module: {max_abs_element}")
    print(f"Ego nomer: {index_max_abs}")