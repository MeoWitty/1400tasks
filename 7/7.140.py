min_radius = float('inf')
import math
while True:
    ploshad = float(input())
    if ploshad == 0:
        break
    radius = math.sqrt(ploshad / math.pi)
    if radius < min_radius:
        min_radius = radius
print(min_radius)