count = 0
i = 500
while count < 20:
    if i % 13 == 0 or i % 17 == 0:
        print(i)
        count += 1
    i += 1