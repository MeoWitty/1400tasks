n = int(input())
temp = n
first = 0
while temp > 0:
    first = temp % 10
    temp //= 10
count_first = 0
temp = n
while temp > 0:
    if temp % 10 == first:
        count_first += 1
    temp //= 10
print(count_first)