max_plotnost = 0
for i in range(20):
    massa = float(input())
    obem = float(input())
    plotnost = massa / obem
    if plotnost > max_plotnost:
        max_plotnost = plotnost
print(max_plotnost)