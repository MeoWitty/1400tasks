n = int(input())
p = int(input())
sum_kratn = 0
count_kratn = 0
for i in range(n):
    a = int(input())
    if a % p == 0:
        sum_kratn += a
        count_kratn += 1
if count_kratn > 0:
    print(sum_kratn / count_kratn)
else:
    print("Нет таких")