sum1 = 0
for i in range(10):
    ball = int(input())
    sum1 += ball

sum2 = 0
for i in range(10):
    ball = int(input())
    sum2 += ball

if sum1 > sum2:
    print("Первый")
elif sum2 > sum1:
    print("Второй")
else:
    print("Равны")