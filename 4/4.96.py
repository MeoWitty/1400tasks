k=int(input())
if k<=50*2:
    num=50+(k-1)//2
    print(num//10 if k%2==1 else num%10)
else:
    k-=50*2
    num=100+(k-1)//3
    pos=(k-1)%3
    print(str(num)[pos])