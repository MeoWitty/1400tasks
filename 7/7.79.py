pobedy = 0
porazheniya = 0
nichii = 0
n = int(input())
for i in range(n):
    ochki = int(input())
    if ochki == 3:
        pobedy += 1
    elif ochki == 0:
        porazheniya += 1
    elif ochki == 1:
        nichii += 1
print(pobedy, porazheniya, nichii)