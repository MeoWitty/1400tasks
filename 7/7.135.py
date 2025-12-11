n = int(input())

# а
max_chislo = float('-inf')
for i in range(n):
    x = float(input())
    if x > max_chislo:
        max_chislo = x
print(max_chislo)

# б
min_chislo = float('inf')
for i in range(n):
    x = float(input())
    if x < min_chislo:
        min_chislo = x
print(min_chislo)

# в
max_chislo = float('-inf')
min_chislo = float('inf')
for i in range(n):
    x = float(input())
    if x > max_chislo:
        max_chislo = x
    if x < min_chislo:
        min_chislo = x
print(max_chislo, min_chislo)