n = int(input())
prostoe = True
for i in range(2, n):
    if n % i == 0:
        prostoe = False
        break
if n > 1 and prostoe:
    print("Да")
else:
    print("Нет")