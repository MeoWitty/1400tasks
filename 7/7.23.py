proizv = 1
n = int(input())
for i in range(n):
    a = int(input())
    proizv *= a
if proizv < 10000:
    print("Да")
else:
    print("Нет")