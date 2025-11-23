a3,a2,a1,b2,b1=int(input()),int(input()),int(input()),int(input()),int(input())
s1=(a1+b1)%10
c1=(a1+b1)//10
s2=(a2+b2+c1)%10
s3=a3+(a2+b2+c1)//10
print(s3,s2,s1)