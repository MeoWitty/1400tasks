h = int(input("h: "))
m = int(input("m: "))
n = 60 * h + m
t0 = (60 * h + m) / 11
c = t0
while c <= n:
    c += 720 / 11
p1 = t0 - 180 / 11
p2 = t0 + 180 / 11
while p1 <= n:
    p1 += 720 / 11
while p2 <= n:
    p2 += 720 / 11
print(int(c - n + 0.999), int(min(p1, p2) - n + 0.999))