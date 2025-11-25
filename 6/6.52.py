r_vnutr = 5
tolshina = 0.5
obem = 0
import math
for i in range(12):
    r_nar = r_vnutr + i * tolshina
    v_shara = (4/3) * math.pi * (r_nar ** 3)
    obem += v_shara
obem_litrov = obem / 1000
print(obem_litrov)