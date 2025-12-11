n = int(input())

# а
max1 = float('-inf')
max2 = float('-inf')
for i in range(n):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
print(max1, max2)

# б
min1 = float('inf')
min2 = float('inf')
for i in range(n):
    x = int(input())
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
print(min1, min2)