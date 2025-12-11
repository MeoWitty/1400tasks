# а
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito > propuscheno:
        print("ВЫИГРЫШ")
    elif zabito < propuscheno:
        print("ПРОИГРЫШ")
    else:
        print("НИЧЬЯ")

# б
pobedy = 0
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito > propuscheno:
        pobedy += 1
print(pobedy)

# в
pobedy = 0
porazheniya = 0
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito > propuscheno:
        pobedy += 1
    elif zabito < propuscheno:
        porazheniya += 1
print(pobedy, porazheniya)

# г
pobedy = 0
porazheniya = 0
nichii = 0
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito > propuscheno:
        pobedy += 1
    elif zabito < propuscheno:
        porazheniya += 1
    else:
        nichii += 1
print(pobedy, nichii, porazheniya)

# д
count = 0
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito - propuscheno >= 3:
        count += 1
print(count)

# е
sum_ochkov = 0
for i in range(20):
    zabito = int(input())
    propuscheno = int(input())
    if zabito > propuscheno:
        sum_ochkov += 3
    elif zabito == propuscheno:
        sum_ochkov += 1
print(sum_ochkov)