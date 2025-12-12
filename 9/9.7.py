pyatok = 0
for u in range(15):
    troek = 0
    for p in range(3):
        o = int(input())
        if o == 5:
            pyatok += 1
        if o == 3:
            troek += 1
    print(troek)
print(pyatok)