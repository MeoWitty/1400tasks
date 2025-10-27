from itertools import permutations
n = input("Введите трёхзначное число с различными цифрами: ")
p = {''.join(x) for x in permutations(n)}
print("Все перестановки:", ', '.join(sorted(p)))