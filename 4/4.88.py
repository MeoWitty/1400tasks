y1,m1=int(input()),int(input())
y2,m2=int(input()),int(input())
y=y2-y1
m=m2-m1
if m<0:y-=1;m+=12
print(y,m)