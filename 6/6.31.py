vklad = 1000

# а
mes = 1
while True:
    uvel = vklad * 0.02
    if uvel > 30:
        print(mes)
        break
    vklad += uvel
    mes += 1

# б
vklad = 1000
mes = 1
while vklad <= 1200:
    vklad *= 1.02
    mes += 1
print(mes)