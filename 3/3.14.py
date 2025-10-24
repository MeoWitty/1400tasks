n = int(input("квартира: "))
print((n - 1) // 54 + 1)
print((n - 1) % 54 // 6 + 1)
print((n - 1) % 6 + 1)