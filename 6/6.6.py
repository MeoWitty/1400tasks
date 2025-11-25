fact = int(input())
n = 1
current = 1
while current < fact:
    n += 1
    current *= n
print(n)