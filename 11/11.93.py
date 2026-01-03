avto = [5000, 6000, 7000, 8000, 9000]
moto = [1000, 2000, 1500, 2500, 3000]
sred_avto = sum(avto) / len(avto)
sred_moto = sum(moto) / len(moto)
if sred_avto > sred_moto * 3:
    print("Verno")
else:
    print("Ne verno")