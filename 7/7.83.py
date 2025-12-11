est_chetnoe = False
n = int(input())
for i in range(n):
    a = int(input())
    if a % 2 == 0:
        est_chetnoe = True
        break
print(est_chetnoe)