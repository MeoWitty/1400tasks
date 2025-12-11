n = int(input())
m = int(input())
p = int(input())
sum_neprev_m = 0
for i in range(n):
    c = int(input())
    if c <= m:
        sum_neprev_m += c
if sum_neprev_m % p == 0:
    print("Да")
else:
    print("Нет")