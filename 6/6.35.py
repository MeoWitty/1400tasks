n = int(input())

# а
count3 = 0
temp = n
while temp > 0:
    if temp % 10 == 3:
        count3 += 1
    temp //= 10
print(count3)

# б
last = n % 10
count_last = 0
temp = n
while temp > 0:
    if temp % 10 == last:
        count_last += 1
    temp //= 10
print(count_last)

# в
count_chet = 0
temp = n
while temp > 0:
    if (temp % 10) % 2 == 0:
        count_chet += 1
    temp //= 10
print(count_chet)

# г
sum_bolshe5 = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra > 5:
        sum_bolshe5 += cifra
    temp //= 10
print(sum_bolshe5)

# д
proizv_bolshe7 = 1
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra > 7:
        proizv_bolshe7 *= cifra
    temp //= 10
print(proizv_bolshe7)

# е
count_05 = 0
temp = n
while temp > 0:
    cifra = temp % 10
    if cifra == 0 or cifra == 5:
        count_05 += 1
    temp //= 10
print(count_05)