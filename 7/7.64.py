count_do1990 = 0
count_posle2000 = 0
n = int(input())
for i in range(n):
    god = int(input())
    if god < 1990:
        count_do1990 += 1
    elif god > 2000:
        count_posle2000 += 1
print(count_do1990, count_posle2000)