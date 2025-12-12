best_group = 0
best_sred = 0
for group in range(3):
    sum_group = 0
    for student in range(20):
        for exam in range(3):
            ball = int(input())
            sum_group += ball
    sred = sum_group / (20 * 3)
    if sred > best_sred:
        best_sred = sred
        best_group = group + 1
print(best_group)