n = int(input())
count_otr = 0
count_polozh = 0
for i in range(n):
    d = float(input())
    if d < 0:
        count_otr += 1
    elif d > 0:
        count_polozh += 1
print(count_otr, count_polozh)