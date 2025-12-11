n = int(input())

# а
p = int(input())
count_bolshe_p = 0
for i in range(n):
    a = int(input())
    if a > p:
        count_bolshe_p += 1
print(count_bolshe_p)

# б
count_okonch_5 = 0
for i in range(n):
    a = int(input())
    if a % 10 == 5:
        count_okonch_5 += 1
print(count_okonch_5)

# в
k = int(input())
count_kratn_k = 0
for i in range(n):
    a = int(input())
    if a % k == 0:
        count_kratn_k += 1
print(count_kratn_k)