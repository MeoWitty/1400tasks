n = float(input())
sum_menwe = 0
pred = None
sled = None
nomer_pred = 0
nomer_sled = 0

count = 0
for i in range(1, 1000):
    y = float(input())
    if y == 10000:
        break
    if y < n:
        sum_menwe += y
    if pred is None and y < n:
        pred = y
        nomer_pred = i
    if y >= n and sled is None:
        sled = y
        nomer_sled = i
    count += 1

print(sum_menwe)
print(nomer_pred, pred, nomer_sled, sled)