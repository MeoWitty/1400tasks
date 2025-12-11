n = int(input())
max_rost = 0
min_rost = float('inf')
for i in range(n):
    rost = float(input())
    if rost > max_rost:
        max_rost = rost
    if rost < min_rost:
        min_rost = rost
print(max_rost - min_rost)