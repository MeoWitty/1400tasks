massiv = [5.5, -3.2, 10.1, -7.8, 0, 15.3, -2.4, 8.6, -1.1, 12.7]
# a)
count_pol = 0
for element in massiv:
    if element > 0:
        count_pol += 1
if count_pol <= 5:
    print("Verno")
else:
    print("Ne verno")

# б)
count_menshe50 = 0
for element in massiv:
    if element <= 50:
        count_menshe50 += 1
if count_menshe50 % 4 == 0:
    print("Verno")
else:
    print("Ne verno")