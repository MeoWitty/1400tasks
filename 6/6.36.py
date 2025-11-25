n = int(input())
a = int(input())

# а
count_a = 0
temp = n
while temp > 0:
    if temp % 10 == a:
        count_a += 1
    temp //= 10
print(count_a)

# б
sum_bolshe_a = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra > a:
        sum_bolshe_a += cifra
    temp //= 10
print(sum_bolshe_a)

# в
sum_chet = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra % 2 == 0:
        sum_chet += cifra
    temp //= 10
print(sum_chet)

# г
x = int(input())
y = int(input())
count_xy = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra == x or cifra == y:
        count_xy += 1
    temp //= 10
print(count_xy)