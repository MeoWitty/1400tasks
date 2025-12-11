n = int(input())
m = int(input())
q = int(input())
sum_neprev_m = 0
for i in range(n):
    a = int(input())
    if a <= m:
        sum_neprev_m += a
if sum_neprev_m > q:
    print("Да")
else:
    print("Нет")