max_osadkov = 0
den_s_max = 0
for den in range(1, 32):
    osadki = float(input())
    if osadki >= max_osadkov:
        max_osadkov = osadki
        den_s_max = den
print(den_s_max)