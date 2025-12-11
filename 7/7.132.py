raznyh = 1
pred = int(input())
for i in range(29):
    tek = int(input())
    if tek != pred:
        raznyh += 1
    pred = tek
print(raznyh)