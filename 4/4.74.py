a2,a1,b2,b1=int(input()),int(input()),int(input()),int(input())
r1=a1-b1+10 if a1<b1 else a1-b1
r2=a2-b2-(1 if a1<b1 else 0)
print(r2,r1)