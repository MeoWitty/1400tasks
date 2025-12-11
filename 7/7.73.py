n = int(input())
count_kratn_3 = 0
count_kratn_7 = 0
for i in range(n):
    x = int(input())
    if x % 3 == 0:
        count_kratn_3 += 1
    if x % 7 == 0:
        count_kratn_7 += 1
print(count_kratn_3, count_kratn_7)