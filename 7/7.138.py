max_temp = float('-inf')
for den in range(30):
    temp = float(input())
    if temp > max_temp:
        max_temp = temp
print(max_temp)