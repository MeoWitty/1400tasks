giri = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
count = 0
for mask in range(1, 1024):
    ves = 0
    for i in range(10):
        if mask & (1 << i):
            ves += giri[i]
    if ves == 5000:
        count += 1
print(count)