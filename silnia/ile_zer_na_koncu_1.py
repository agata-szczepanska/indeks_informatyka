from math import factorial

s = str(factorial(100))
zera = len(s) - len(s.rstrip("0"))
print(zera)