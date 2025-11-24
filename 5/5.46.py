n = int(input())
ch1, ch2 = 1, 2
zn1, zn2 = 1, 1
print(ch1 / zn1)
print(ch2 / zn2)
for i in range(3, n + 1):
    ch_n = ch1 + ch2
    zn_n = zn1 + zn2
    print(ch_n / zn_n)
    ch1, ch2 = ch2, ch_n
    zn1, zn2 = zn2, zn_n