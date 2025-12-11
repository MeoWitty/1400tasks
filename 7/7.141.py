max_diagonal = 0
import math
while True:
    ploshad = float(input())
    if ploshad == 0:
        break
    storona = math.sqrt(ploshad)
    diagonal = storona * math.sqrt(2)
    if diagonal > max_diagonal:
        max_diagonal = diagonal
print(max_diagonal)