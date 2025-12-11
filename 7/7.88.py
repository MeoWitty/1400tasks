n = int(input())
x = int(input())
count_otr = 0
for i in range(n):
    a = int(input())
    if a < 0:
        count_otr += 1
if count_otr > x:
    print("Да")
else:
    print("Нет")