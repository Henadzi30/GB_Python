# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint


n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
some_list_n = [int(input('Элемент 1-го множества: ')) for _ in range(n)]
print(* some_list_n)
some_list_m = [int(input('Элемент 2-го множества: ')) for _ in range(m)]
print(* some_list_m)
print(* sorted(set(some_list_n).intersection(set(some_list_m))))


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом
# кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора
# черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста
# и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9


blueberry_bushes = [int(randint(1, 25)) for _ in range(
    int(input('Введите кол-во кустов черники: ')))]
print(* blueberry_bushes)
more_berries = 0
for i in range(2, len(blueberry_bushes)):
    summ_berries = blueberry_bushes[i - 2] + blueberry_bushes[i - 1] + blueberry_bushes[i]
    if summ_berries > more_berries:
        more_berries = summ_berries      
print(more_berries)