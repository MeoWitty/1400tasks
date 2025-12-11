max_rasstoyanie = 0
while True:
    gorod = input()
    if gorod == "end":
        break
    rasstoyanie = float(input())
    if rasstoyanie > max_rasstoyanie:
        max_rasstoyanie = rasstoyanie
print(max_rasstoyanie)