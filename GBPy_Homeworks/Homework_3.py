from random import randint
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

# 5
# 1 2 3 4 5
# 3
# -> 1

len_array = int(input('Введите количество элементов в массиве: '))
array_A = []
for _ in range(len_array):
    array_A.append(randint(0, 9))
print(* array_A)
num_X = int(input('Введите число для поиска его в массиве: '))
count_X = 0
for i in range(len(array_A)):
    if array_A[i] == num_X:
        count_X += 1
print(count_X)

# Решение в другом виде
a = [int(input()) for _ in range(int(input()))]
x = int(input('Введите искомое число: '))
print(a.count(x))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X.

# 5
# 1 2 3 4 5
# 6
# -> 5

len_arr_N = int(input('Введите количество элементов в массиве: '))
array_B = [] # Формируем и заполняем случайными числами список заданной длины
for _ in range(len_arr_N):
    array_B.append(randint(0, 9))
print(* array_B) # Выводим список в консоль
swapped = True # Упорядочиваем список по возрастанию
while swapped:
    swapped = False
    for i in range(len(array_B) - 1):
        if array_B[i] > array_B[i + 1]:
            # Меняем элементы
            array_B[i], array_B[i + 1] = array_B[i + 1], array_B[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
array_Bb = [] # Формируем список с уникальными значениями
for j in range(len(array_B)):
    if array_B[j] in array_Bb:
        continue
    else:
        array_Bb.append(array_B[j])           
num_X = int(input('Введите число X: '))
desired_number_to = 0 # Перебираем список с уникальными значениями для выбора наиболее близких к заданному
desired_number_after = 0
flag = False
for k in range(1, len(array_Bb)):
    if num_X == array_Bb[k]:
        flag = True

    if num_X != array_Bb[k] and array_Bb[k - 1] <= num_X <= array_Bb[k]:
        desired_number_to = array_Bb[k - 1]
        desired_number_after = array_Bb[k]
to = abs(num_X - desired_number_to)
after = abs(num_X - desired_number_after)
if flag: print(num_X)
if not flag and to == after:
    print(f'или {desired_number_to}, или {desired_number_after}')
elif not flag and 2 <= to > after:
    print(desired_number_after)
elif not flag and 2 <= after > to:
    print(desired_number_to)        

# number = abs(num_X - array_B[0])
# ind = 0
# for i in range(len_arr_N):
#     count = abs(num_X - array_B[i])
#     if count < number:
#         number = count
#         ind = i
# print(array_B[ind])

# Решение в другом виде
rnd_list = [random.randint(-100, 100) for _ in range(10)]
x = int(input())
print(rnd_list)
min_diff = abs(rnd_list[0] - x)
for el in rnd_list:
    if abs(el - x) < min_diff:
        min_diff = abs(el - x)
        find_el = el
print(find_el)

# Еще вариант

rnd_list = [random.randint(-100, 100) for _ in range(10)]
x = int(input())
print(rnd_list)
some_set = set(rnd_list)
diff = 0
while True:
    if x + diff in some_set:
        print(x + diff)
        break
    elif x - diff in some_set:
        print(x - diff)
        break
    diff += 1


# Задача 20: В настольной игре Скрабл(Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко
# ● D, G – 2 очка
# ● B, C, M, P – 3 очка
# ● F, H, V, W, Y – 4 очка
# ● K – 5 очков
# ● J, X – 8 очков
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко
# ● Д, К, Л, М, П, У – 2 очка
# ● Б, Г, Ё, Ь, Я – 3 очка
# ● Й, Ы – 4 очка
# ● Ж, З, Х, Ц, Ч – 5 очков
# ● Ш, Э, Ю – 8 очков
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

word = input('Enter the word: ').upper()
# en A = 65 - 90; a = 97 - 122
# ru A = 1040 - 1071; а = 1072 - 1103
english_letters = {1: 'AEIOULNSTR',
                    2: 'DG',
                    3: 'BCMP',
                    4: 'FHVWY',
                    5: 'K',
                    8: 'JX',
                    10: 'QZ'}
kirylic_letters = {1: 'АВЕИНОРСТ',
                    2: 'ДКЛМПУ',
                    3: 'БГЁЬЯ',
                    4: 'ЙЫ',
                    5: 'ЖЗХЦЧ',
                    8: 'ШЭЮ',
                    10: 'ФЩЪ'}
sum_en = 0
if 65 <= ord(word[0]) <= 90:   
    for i in range(len(word)):
        for k, v in english_letters.items():
            if word[i] in v:
                sum_en += k
else:
    for j in range(len(word)):
        for k, v in kirylic_letters.items():
            if word[j] in v:
                sum_en += k
print(sum_en)

# Решение в другом виде
dictionary =    {
                'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
                'D': 2, 'G': 2,
                'B': 3, 'C': 3, 'M': 3, 'P': 3,
                'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                'K': 5,
                'J': 8, 'X': 8, 
                'Q': 10, 'Z': 10
                }
summa = 0
for letter in input():
    summa += dictionary[letter]
print(summa)
