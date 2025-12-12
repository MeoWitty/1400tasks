bez_troek = 0
for student in range(14):
    troek = 0
    for predmet in range(3):
        o = int(input())
        if o == 3:
            troek += 1
    if troek == 0:
        bez_troek += 1
print(bez_troek)