import math
e = float(input("e: "))
f = float(input("f: "))
g = float(input("g: "))
h = float(input("h: "))
a = (e + f/2) / 3
b = abs(h**2 - g)
c = math.sqrt((g - h)**2 - 3 * math.sin(e))
print("a =", a)
print("b =", b)
print("c =", c)