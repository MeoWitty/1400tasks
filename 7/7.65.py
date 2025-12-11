count_bolshe = 0
n = int(input())
for i in range(n):
    pobedy = int(input())
    porazheniya = int(input())
    if pobedy > porazheniya:
        count_bolshe += 1
print(count_bolshe)