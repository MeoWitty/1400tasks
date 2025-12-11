min_plotnost = float('inf')
for i in range(16):
    naselenie = float(input())
    ploshad = float(input())
    plotnost = naselenie / ploshad
    if plotnost < min_plotnost:
        min_plotnost = plotnost
print(min_plotnost)