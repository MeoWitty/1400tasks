n = int(input())

# а
count_ravenstvo = 0
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if tek == pred:
        count_ravenstvo += 1
    pred = tek
print(count_ravenstvo)

# б
count_nuley = 0
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if pred == 0 and tek == 0:
        count_nuley += 1
    pred = tek
print(count_nuley)

# в
count_nechet = 0
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if pred % 2 != 0 and tek % 2 != 0:
        count_nechet += 1
    pred = tek
print(count_nechet)

# г
count_okonch_5 = 0
pred = int(input())
for i in range(n - 1):
    tek = int(input())
    if pred % 10 == 5 and tek % 10 == 5:
        count_okonch_5 += 1
    pred = tek
print(count_okonch_5)