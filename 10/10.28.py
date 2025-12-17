import random

vsego = 1000000
v_kruge = 0

for i in range(vsego):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y <= 1:
        v_kruge += 1

pi = 4 * (v_kruge / vsego)
print(f"Priblizitelnoe znachenie pi: {pi}")