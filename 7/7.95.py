n = int(input())
count_smen = 0
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if (pred > 0 and tek < 0) or (pred < 0 and tek > 0):
        count_smen += 1
    pred = tek
print(count_smen)