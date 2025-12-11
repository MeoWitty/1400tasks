min_temp = float('inf')
count_min_dney = 0
for den in range(1, 32):
    temp = float(input())
    if temp < min_temp:
        min_temp = temp
        count_min_dney = 1
    elif temp == min_temp:
        count_min_dney += 1
print(count_min_dney)