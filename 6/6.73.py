m = int(input())
g = int(input())
z = int(input())
while g < m:
    g *= z
if g == m:
    print("Да")
else:
    print("Нет")