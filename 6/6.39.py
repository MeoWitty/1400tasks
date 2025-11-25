n = int(input())
temp = n
count = 0
while temp > 0:
    count += 1
    temp //= 10
while count > 0:
    step = 10 ** (count - 1)
    print(n // step % 10)
    count -= 1