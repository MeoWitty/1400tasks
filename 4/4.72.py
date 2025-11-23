x1,y1,w1,h1=float(input()),float(input()),float(input()),float(input())
x2,y2,w2,h2=float(input()),float(input()),float(input()),float(input())
a=x1>=x2 and y1>=y2 and x1+w1<=x2+w2 and y1+h1<=y2+h2
b=a or (x2>=x1 and y2>=y1 and x2+w2<=x1+w1 and y2+h2<=y1+h1)
c=not(x1+w1<x2 or x2+w2<x1 or y1+h1<y2 or y2+h2<y1)
print(a,b,c)