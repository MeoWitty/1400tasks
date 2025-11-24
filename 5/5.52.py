import math
r_vnutr = 5  # см
tolshina = 0.5  # см
obem = 0
for i in range(12):
    r_nar = r_vnutr + i * tolshina
    v_shara = (4/3) * math.pi * (r_nar ** 3)
    obem += v_shara
obem_ml = obem  # см³
obem_litrov = obem_ml / 1000
print(obem_litrov)