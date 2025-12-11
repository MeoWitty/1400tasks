rost_novogo = float(input())
mesto = 1
for i in range(15):
    rost = float(input())
    if rost > rost_novogo:
        mesto += 1
print(mesto)