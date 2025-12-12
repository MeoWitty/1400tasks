min_kurs = 1000
for kurs in range(4):
    sum_kurs = 0
    max_group = 0
    max_group_num = 0
    for group in range(6):
        stud = int(input())
        sum_kurs += stud
        if stud > max_group:
            max_group = stud
            max_group_num = group + 1
    if sum_kurs < min_kurs:
        min_kurs = sum_kurs
        min_kurs_num = kurs + 1
    print(max_group_num)
print(min_kurs_num)