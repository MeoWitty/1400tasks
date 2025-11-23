a, b, c, x, y = float(input()), float(input()), float(input()), float(input()), float(input())
sides = [(a, b), (a, c), (b, c)]
for side1, side2 in sides:
    if (side1 <= x and side2 <= y) or (side1 <= y and side2 <= x):
        print("Да")
        break
else:
    print("Нет")