num1 = 1
den1 = 1
num2 = 2
den2 = 1
while abs(num2 / den2 - num1 / den1) > 0.001:
    num1, num2 = num2, num1 + num2
    den1, den2 = den2, den1 + den2
print(num2 / den2)