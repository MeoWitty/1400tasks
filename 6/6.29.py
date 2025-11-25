count = 0
i = 100
while count < 10:
    if i % 10 == 7 and i % 9 == 0:
        print(i)
        count += 1
    i += 1