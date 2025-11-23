n=int(input())
a=int(input())
s=0
for i in range(n):
    s+=a+i
print(s%2==0)