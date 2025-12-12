total_quarter = 0
for rabotnik in range(12):
    sum_rab = 0
    for mesac in range(3):
        z = int(input())
        sum_rab += z
        total_quarter += z
    print(sum_rab)
print(total_quarter)