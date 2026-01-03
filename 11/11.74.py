massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
a = int(input())
b = int(input())
count = 0
for element in massiv:
    if a <= element <= b:
        count += 1
print(count)