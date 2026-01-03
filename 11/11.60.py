massiv = [5, 8, 12, 3, 7, 9, 11, 15, 2, 6]
# a)
summa_nechet = 0
for element in massiv:
    if element % 2 != 0:
        summa_nechet += element
print(summa_nechet)

# б)
k = int(input())
summa_krat = 0
for element in massiv:
    if element % k == 0:
        summa_krat += element
print(summa_krat)

# в)
q = int(input())
p = int(input())
summa_krat_q_p = 0
for element in massiv:
    if element % q == 0 and element % p == 0:
        summa_krat_q_p += element
print(summa_krat_q_p)