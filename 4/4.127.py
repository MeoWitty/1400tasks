a,b,c=int(input()),int(input()),int(input())
mx=max(a,b,c);mn=min(a,b,c);md=a+b+c-mx-mn
print("первое" if a==mx else "второе" if b==mx else "третье")
print("первое" if a==mn else "второе" if b==mn else "третье")
print("первое" if a==md else "второе" if b==md else "третье")