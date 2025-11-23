n,m=int(input()),int(input())
md=[31,28,31,30,31,30,31,31,30,31,30,31]
if n>1:print(n-1,m)
else:print(md[m-2],m-1)
if n<md[m-1]:print(n+1,m)
else:print(1,m+1)