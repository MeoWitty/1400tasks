massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
if massiv:
    max_element = max(massiv)
    min_element = min(massiv)
    if max_element % 2 == 0:
        print("Maximum - chetnoe")
    else:
        print("Maximum - nechetnoe")
    if min_element % 2 == 0:
        print("Minimum - chetnoe")
    else:
        print("Minimum - nechetnoe")