max_povtor = 1
tek_povtor = 1
pred = int(input())
while True:
    tek = int(input())
    if tek == 1000:
        break
    if tek == pred:
        tek_povtor += 1
        if tek_povtor > max_povtor:
            max_povtor = tek_povtor
    else:
        tek_povtor = 1
    pred = tek
print(max_povtor)