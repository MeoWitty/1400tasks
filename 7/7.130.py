povtoreniy = 0
pred = int(input())
for i in range(19):
    tek = int(input())
    if tek == pred:
        povtoreniy += 1
    pred = tek
print(povtoreniy)