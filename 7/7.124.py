N = int(input())
mesto = 1
for i in range(20):
    ochki = int(input())
    if ochki > N:
        mesto += 1
print(mesto)