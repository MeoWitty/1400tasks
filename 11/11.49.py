massiv = [5, 25, 12, 30, 7, 18, 21, 15, 22, 6]
# a)
summa = 0
for element in massiv:
    if element <= 20:
        summa += element
print(summa)

# б)
a = int(input())
summa = 0
for element in massiv:
    if element > a:
        summa += element
print(summa)