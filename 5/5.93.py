n = int(input())
sum_del = 0
for i in range(1, n):
    if n % i == 0:
        sum_del += i
if sum_del == n:
    print("Да")
else:
    print("Нет")