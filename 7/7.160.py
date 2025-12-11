min_vremya = float('inf')
nomer_pobeditelya = 0
for i in range(1, 21):
    vremya = float(input())
    if vremya < min_vremya:
        min_vremya = vremya
        nomer_pobeditelya = i
print(nomer_pobeditelya)