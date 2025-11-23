g,m,n=int(input()),int(input()),int(input())
leap=g%400==0 or(g%4==0 and g%100!=0)
md=[31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]
if n>1:print(n-1,m,g)
else:print(md[m-2],m-1,g)
if n<md[m-1]:print(n+1,m,g)
else:print(1,m+1,g)