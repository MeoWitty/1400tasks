# a
rasstoyanie = 0
znak = 1
for i in range(1, 101):
    rasstoyanie += znak * (1 / i)
    znak = -znak
print(rasstoyanie)

# б
put = 0
for i in range(1, 101):
    put += 1 / i
print(put)