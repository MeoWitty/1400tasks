x=float(input())
# а) y = -1 при x < 0, y = 1 при x >= 0
print(-1 if x<0 else 1)
x=float(input())
# б) y = 1 при x < 0, y = -1 при x >= 0
print(1 if x<0 else -1)
x=float(input())
# в) y = -1 при x < 0, y = 0 при x = 0, y = 1 при x > 0
print(-1 if x<0 else 1 if x>0 else 0)
