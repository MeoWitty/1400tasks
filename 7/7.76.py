komanda1_udal = 0
komanda1_vremya = 0
komanda2_udal = 0
komanda2_vremya = 0

for i in range(24):
    nomer = int(input())
    vremya = int(input())
    if nomer == 1:
        komanda1_udal += 1
        komanda1_vremya += vremya
    else:
        komanda2_udal += 1
        komanda2_vremya += vremya

print(komanda1_udal, komanda1_vremya)
print(komanda2_udal, komanda2_vremya)