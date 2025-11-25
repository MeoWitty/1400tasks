probeg = 10

# а
den = 1
while probeg <= 20:
    probeg *= 1.1
    den += 1
print(den)

# б
probeg = 10
summa = 10
den = 1
while summa <= 100:
    probeg *= 1.1
    summa += probeg
    den += 1
print(den)