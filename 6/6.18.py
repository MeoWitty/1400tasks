import math
a = int(input())
b = int(input())

# а
i = a
while i <= b:
    print(math.sqrt(i))
    i += 1

# б
i = a
while True:
    print(math.sqrt(i))
    i += 1
    if i > b:
        break