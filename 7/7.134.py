raznyh = 1
pred = float(input())
while True:
    tek = float(input())
    if tek == 10000:
        break
    if tek != pred:
        raznyh += 1
    pred = tek
print(raznyh)