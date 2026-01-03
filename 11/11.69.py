massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
# a)
last = massiv[-1]
count = 0
for element in massiv:
    if element != last:
        count += 1
print(count)

# б)
a = int(input())
count = 0
for element in massiv:
    if element % a == 0:
        count += 1
print(count)