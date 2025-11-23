a,b,c,d,e,f=int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
rt=lambda x1,y1,x2,y2:x1==x2 or y1==y2
bs=lambda x1,y1,x2,y2:abs(x1-x2)==abs(y1-y2)
qn=lambda x1,y1,x2,y2:rt(x1,y1,x2,y2) or bs(x1,y1,x2,y2)
kn=lambda x1,y1,x2,y2:(abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2)
print(rt(a,b,e,f) and not rt(c,d,e,f))