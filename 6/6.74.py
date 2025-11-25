n = int(input())

# а
temp = n
while temp % 3 == 0:
    temp //= 3
if temp == 1:
    print("Да")
else:
    print("Нет")

# б
temp = n
while temp % 5 == 0:
    temp //= 5
if temp == 1:
    print("Да")
else:
    print("Нет")