for znamen in range(2, 8):
    for chisl in range(1, znamen):
        prostoe = True
        for d in range(2, chisl + 1):
            if chisl % d == 0 and znamen % d == 0:
                prostoe = False
                break
        if prostoe:
            print(chisl, '/', znamen)