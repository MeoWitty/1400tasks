count = 0
n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and a + c > b and b + c > a:
        count += 1
print(count)