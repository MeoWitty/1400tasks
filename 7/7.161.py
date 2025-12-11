min_ochkov = float('inf')
nomer_komandy = 0
while True:
    komanda = int(input())
    if komanda == 0:
        break
    ochki = int(input())
    if ochki < min_ochkov:
        min_ochkov = ochki
        nomer_komandy = komanda
print(nomer_komandy)