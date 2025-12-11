sum_chet = 0
count_chet = 0
sum_nechet = 0
count_nechet = 0
for i in range(12):
    a = int(input())
    if a % 2 == 0:
        sum_chet += a
        count_chet += 1
    else:
        sum_nechet += a
        count_nechet += 1
print(sum_chet / count_chet, sum_nechet / count_nechet)