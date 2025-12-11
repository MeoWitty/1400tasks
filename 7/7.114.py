sum_chet = 0
count_chet = 0
n = int(input())
for i in range(n):
    d = int(input())
    if d % 2 == 0:
        sum_chet += d
        count_chet += 1
if count_chet > 0:
    print(sum_chet / count_chet)
else:
    print("Нет таких")