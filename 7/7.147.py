max_uchenikov = 0
min_uchenikov = float('inf')
for i in range(20):
    ucheniki = int(input())
    if ucheniki > max_uchenikov:
        max_uchenikov = uchenikov
    if uchenikov < min_uchenikov:
        min_uchenikov = uchenikov
print(max_uchenikov - min_uchenikov)