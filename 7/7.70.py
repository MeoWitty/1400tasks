# 1 случай
dney = 0
for den in range(1, 32):
    osadki = float(input())
    if osadki > 0:
        break
    dney += 1
print(dney)

# 2 случай
dney = 0
for den in range(1, 32):
    osadki = float(input())
    if osadki > 0:
        dney = 0
    else:
        dney += 1
print(dney)