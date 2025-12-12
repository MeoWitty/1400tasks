# а)
S = int(input())
for a in range(1, S + 1):
    for b in range(1, S + 1):
        if a * b == S:
            print(a, b)

# б)
S = int(input())
for a in range(1, int(S**0.5) + 1):
    if S % a == 0:
        b = S // a
        print(a, b)