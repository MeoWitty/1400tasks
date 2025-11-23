m=int(input())
leap=input()=="да"
days=[31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]
print(days[m-1])