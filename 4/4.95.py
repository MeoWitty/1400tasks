n=int(input())
if n==1:print(0)
else:
    k=n-2
    num=1+k//2
    print(num//10 if k%2==0 else num%10)