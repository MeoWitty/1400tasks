max_chetnoe = -1
for i in range(14):
    chislo = int(input())
    if chislo % 2 == 0 and chislo > max_chetnoe:
        max_chetnoe = chislo
if max_chetnoe == -1:
    print("Нет четных")
else:
    print(max_chetnoe)