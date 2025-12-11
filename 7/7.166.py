min_tok = float('inf')
nomer_soprotivleniya = 0
for i in range(1, 21):
    napryazhenie = float(input())
    soprotivlenie = float(input())
    tok = napryazhenie / soprotivlenie
    if tok < min_tok:
        min_tok = tok
        nomer_soprotivleniya = i
print(nomer_soprotivleniya)