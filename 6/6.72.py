n = int(input())
f = int(input())
s = int(input())
while f < n:
    f += s
if f == n:
    print("Да")
else:
    print("Нет")