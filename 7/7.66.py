n = int(input())
count_otr = 0
pred = 0
for i in range(n):
    a = float(input())
    if i == 0 and a < 0:
        count_otr += 1
    elif a < 0 and pred >= 0:
        count_otr += 1
    pred = a
print(count_otr)