n = int(input())
rub = n // 100
kop = n % 100
if rub == 0:
    print(f"{kop} копеек")
elif kop == 0:
    if rub % 10 == 1 and rub % 100 != 11:
        print(f"{rub} рубль ровно")
    elif 2 <= rub % 10 <= 4 and (rub % 100 < 10 or rub % 100 >= 20):
        print(f"{rub} рубля ровно")
    else:
        print(f"{rub} рублей ровно")
else:
    if rub % 10 == 1 and rub % 100 != 11:
        print(f"{rub} рубль {kop} копеек")
    elif 2 <= rub % 10 <= 4 and (rub % 100 < 10 or rub % 100 >= 20):
        print(f"{rub} рубля {kop} копеек")
    else:
        print(f"{rub} рублей {kop} копеек")