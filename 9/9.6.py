sportsmen = 15
vid = 3
for s in range(sportsmen):
    sum_s = 0
    for v in range(vid):
        b = int(input())
        sum_s += b
    print(sum_s / vid)

for v in range(vid):
    sum_v = 0
    for s in range(sportsmen):
        b = int(input())
        sum_v += b
    print(sum_v / sportsmen)