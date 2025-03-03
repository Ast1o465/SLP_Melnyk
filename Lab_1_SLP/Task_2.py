number_n = int(input("Введіть число: "))
temp = 0

for i in range(1, number_n):
    if number_n % i == 0:
        temp += i

if temp == number_n:
    print("число досконале")
else:
    print("число не досконале")