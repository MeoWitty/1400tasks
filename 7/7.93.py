est_moschnost = False
for i in range(30):
    moschnost = float(input())
    if moschnost > 200:
        est_moschnost = True
        break
print(est_moschnost)