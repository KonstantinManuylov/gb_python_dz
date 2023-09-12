# (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива.
# затем размер второго массива M
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности сохранить исходный
# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

from random import randint

n = random.randint(5, 10)
m = random.randint(5, 10)

list_1 = [random.randint(1, 10) for i in range(n)]
list_2 = [random.randint(1, 10) for j in range(m)]

print(n, list_1)
print(m, list_2)

list_3 = [num for num in list_1 if num not in list_2]

print(list_3)
