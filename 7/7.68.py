n = int(input())
count = 1
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if tek != pred:
        break
    count += 1
print(count)