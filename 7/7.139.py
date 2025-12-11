max_skorost = 0
for i in range(20):
    skorost = float(input())
    if skorost > max_skorost:
        max_skorost = skorost
print(max_skorost)