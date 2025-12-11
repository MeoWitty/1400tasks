n = int(input())

# а
max_srednee = 0
nomer_poslednego_max = 0
for i in range(1, n+1):
    a = float(input())
    b = float(input())
    srednee = (a + b) / 2
    if srednee > max_srednee:
        max_srednee = srednee
        nomer_poslednego_max = i
    elif srednee == max_srednee:
        nomer_poslednego_max = i
print(nomer_poslednego_max)

# б
min_srednee_geom = float('inf')
nomer_pervogo_min = 0
for i in range(1, n+1):
    a = float(input())
    b = float(input())
    import math
    srednee_geom = math.sqrt(a * b)
    if srednee_geom < min_srednee_geom:
        min_srednee_geom = srednee_geom
        nomer_pervogo_min = i
    elif srednee_geom == min_srednee_geom and nomer_pervogo_min == 0:
        nomer_pervogo_min = i
print(nomer_pervogo_min)