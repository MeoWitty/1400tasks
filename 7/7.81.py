pobedy = 0
porazheniya = 0
nichii = 0
for i in range(20):
    chislo = int(input())
    zabito = chislo // 10
    propuscheno = chislo % 10
    if zabito > propuscheno:
        pobedy += 1
    elif zabito < propuscheno:
        porazheniya += 1
    else:
        nichii += 1
print(pobedy, porazheniya, nichii)