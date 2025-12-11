sum_chet = 0
sum_nechet = 0
while True:
    dom = int(input())
    if dom == 0:
        break
    zhiteli = int(input())
    if dom % 2 == 0:
        sum_chet += zhiteli
    else:
        sum_nechet += zhiteli
if sum_chet > sum_nechet:
    print("Четная")
else:
    print("Нечетная")