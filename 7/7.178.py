n = int(input())

# а
max_chislo = float('-inf')
nomer_max = 0
count_max = 0
for i in range(1, n+1):
    a = int(input())
    if a > max_chislo:
        max_chislo = a
        nomer_max = i
        count_max = 1
    elif a == max_chislo:
        count_max += 1
if count_max == 1:
    print(nomer_max)

# б
min_chislo = float('inf')
nomer_min = 0
count_min = 0
for i in range(1, n+1):
    a = int(input())
    if a < min_chislo:
        min_chislo = a
        nomer_min = i
        count_min = 1
    elif a == min_chislo:
        count_min += 1
if count_min == 1:
    print(nomer_min)