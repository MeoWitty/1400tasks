# а)
V = int(input())
for a in range(1, V + 1):
    for b in range(1, V + 1):
        for c in range(1, V + 1):
            if a * b * c == V:
                print(a, b, c)

# б)
V = int(input())
for a in range(1, int(V**(1/3)) + 1):
    if V % a == 0:
        V2 = V // a
        for b in range(a, int(V2**0.5) + 1):
            if V2 % b == 0:
                c = V2 // b
                if c >= b:
                    print(a, b, c)