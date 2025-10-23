dlina = float(input("Введите длину: "))
shirina = float(input("Введите ширину: "))
visota = float(input("Введите высоту: "))
obiem = dlina * shirina * visota
ploshad = 2 * visota * (dlina + shirina)
print("Объем:" + str(obiem))
print("Площадь боковой поверхности:" + str(ploshad))