massiv = [150, 160, 170, 165, 155, 175, 180, 172, 168, 162, 158, 152, 148, 145, 140, 135, 130, 125, 120, 115, 110, 105]
r = int(input())
count = 0
for element in massiv:
    if element <= r:
        count += 1
print(count)