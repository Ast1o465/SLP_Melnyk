import random

num_array = int(input("Введіть кількість елементів в масиві:\n"))
if num_array <= 0:
    print("Помилка! Кількість елементів має бути більше 0")
    exit()

array = [round(random.uniform(-10,10), 2)for _ in range(num_array)] #створення масиву з рандомними числами
min_num = min(array) #мінімальне число масиву

dodatni_chusla = [num for num in array if num > 0]
dodatni_chusla= dodatni_chusla[::-1]

zero_num_in_array = False
temp = 1

for num in array:
    if num != 0:
        temp *= num
        zero_num_in_array = True

print("Початковий масив:\n", array)
print("мінімальне число масиву\n", min_num)
print("додатні елементи масиву у зворотному порядку\n", dodatni_chusla)

if zero_num_in_array:
    print("Добуток ненульових елементів:\n", temp)
else:
    print("У масиві немає ненульових елементів\n")


