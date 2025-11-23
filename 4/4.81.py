a, b, c = float(input()), float(input()), float(input())
if a + b > c and a + c > b and b + c > a:
    sides = sorted([a, b, c])
    print(abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6)
else:
    print("Не треугольник")