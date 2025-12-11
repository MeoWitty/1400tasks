import math
n = int(input())
H = float(input())
R = float(input())
popadaniya = 0
for i in range(n):
    alpha = float(input())
    v0 = float(input())
    t = R / (v0 * math.cos(math.radians(alpha)))
    y = v0 * t * math.sin(math.radians(alpha)) - 9.8 * t * t / 2
    if abs(y - H) < 0.1:
        popadaniya += 1
print(popadaniya / n * 100)