n = int(input())
max_dlina = 0
tek_dlina = 0
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        tek_dlina += 1
        if tek_dlina > max_dlina:
            max_dlina = tek_dlina
    else:
        tek_dlina = 0
print(max_dlina)