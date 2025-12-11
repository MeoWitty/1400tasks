n = int(input())
s = float(input())
proizv = 1
for i in range(n):
    d = float(input())
    proizv *= d
if proizv > s:
    print("Да")
else:
    print("Нет")