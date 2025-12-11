sum_ploshad = 0
sum_uroj = 0
for i in range(10):
    ploshad = float(input())
    urozhainost = float(input())
    sum_ploshad += ploshad
    sum_uroj += ploshad * urozhainost
print(sum_uroj, sum_uroj / sum_ploshad)