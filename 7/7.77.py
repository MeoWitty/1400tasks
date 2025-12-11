komanda1_udal = 0
komanda1_vremya = 0
komanda2_udal = 0
komanda2_vremya = 0

while True:
    komanda = int(input())
    if komanda == 0:
        break
    vremya = int(input())
    if komanda == 1:
        komanda1_udal += 1
        komanda1_vremya += vremya
    else:
        komanda2_udal += 1
        komanda2_vremya += vremya

print(komanda1_udal, komanda1_vremya)
print(komanda2_udal, komanda2_vremya)