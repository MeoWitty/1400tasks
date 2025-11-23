a1, a2, a3 = float(input()), float(input()), float(input())
b1, b2, b3 = float(input()), float(input()), float(input())
box_sides = [b1, b2, b3]
case_sides = [a1, a2, a3]
box_sides.sort()
case_sides.sort()
print(box_sides[0] <= case_sides[0] and box_sides[1] <= case_sides[1] and box_sides[2] <= case_sides[2])