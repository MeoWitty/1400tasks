max_class = 0
for p in range(3):
    for k in range(4):
        uch = int(input())
        if uch > max_class:
            max_class = uch
print(max_class)