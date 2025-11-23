import math
a,v,R,H,P=float(input()),float(input()),float(input()),float(input()),float(input())
g=9.8
t=R/(v*math.cos(math.radians(a)))
y=v*t*math.sin(math.radians(a))-g*t*t/2
print(H<=y<=H+P)