# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_el = int(input('Введите первый элемент массива: '))
diferent_el = int(input('Введите разность элементов: '))
count_el = int(input('Введите количество элементов в массиве: '))
my_list = []
for i in range(1, count_el + 1):
    my_list.append(first_el + (i - 1) * diferent_el)
print(* my_list)


# Задача 32: Определить индексы элементов массива(списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

len_list = int(input('Введите длину массива: '))
my_list_2 = []
for i in range(len_list):
    my_list_2.append(int(input(f'{i} элемент массива: ')))
min_element, max_element = int(input('Введите минимальное значение элемента списка: ')), int(input('Введите максимальное значение элемента списка: '))
list_index = []
for j in range(len_list):
    if min_element <= my_list_2[j] <= max_element:
        list_index.append(j)
print(* my_list_2)
print(* list_index)

