import math

m = int(input("Введіть M\n"))
n = int(input("Введіть N\n"))

if m <= 0 or n < 0:
    print("ERROR!!")
else:
    z = (math.sqrt(m) - math.sqrt(n)) / m
    print(z)
