# Задача №25. Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса
# формата _n.

# Input: a a a b c a a d c d d

# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# import random
# some_str = ''.join([chr(random.randint(65, 100)) for _ in range(10 ** 5)])        # input('>>> ')

# import time
# start = time.perf_counter()
# for letter in set(some_str):
#     # print(f'{letter}_{some_str.count(letter)}', end=', ')
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start


# start2 = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1:
#             amount += 1
#     b = letter, amount
# end2 = time.perf_counter()
# duration2 = end2 - start2
# # print(duration2 / duration1)


# start3 = time.perf_counter()
# count = 0
# lens = len(some_str)
# while lens > 0:
#     for i in range(lens):
#         if some_str[0] == some_str[i]:
#             count += 1
#     lens -= count
#     # print(f'{some_str[0]} -> {count}')
#     c = f'{some_str[0]} -> {count}'
#     some_str = some_str.replace(some_str[0], '')
#     count = 0
# end3 = time.perf_counter()
# duration3 = end3 - start3
# # print(duration1, duration2, duration3)

# # print(some_str)
# start4 = time.perf_counter()
# count_dict = {} # a: 3
# for letter in some_str:
#     if letter not in count_dict:
#         count_dict[letter] = 1
#     else:
#         count_dict[letter] += 1
# # print(count_dict)
# end4 = time.perf_counter()
# duration4 = end4 - start4
# print(duration1, duration2, duration3, duration4)

# Задача №27. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов. Определите, сколько
# различных слов содержится в этом тексте. split

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

# some_str = input('>>> ').split()
# print(len(set(some_str)))

# some_str = input('>>> ')
# some_set = set()
# temp_word = ''
# for letter in some_str:
#     if letter != ' ':
#         temp_word += letter
#     else:
#         if temp_word:
#             some_set.add(temp_word)
#         temp_word = ''
# some_set.add(temp_word)
# print(some_set)
# print(len(some_set))

# Задача №29. Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность неотрицательных
# целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся
# нулем(число 0 не входит в последовательность)”. Однако 2 друга
# оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше
# ошибок в коде, тот и выиграл спор. За помощью товарищи обратились
# к Вам, студентам.

# Ваня:
# n = int(input('>>> '))
# max_number = 0
# while n != 0:
#     n = int(input('>>> '))
#     if max_number < n:  # было if max_number > n:
#         max_number = n
# print(max_number)

# Петя:
n = int(input('>>> '))
max_number = -1
while n > 0:  # Было while n < 0:
    n = int(input('>>> '))
    if max_number < n:
       max_number = n   # Было n = max_number
print(max_number)  # Было print(n)



# some_string = input("Enter the worlds: ")
# some_set = set(some_string)

# for item in some_set:
#     print(f'{item} is {some_string.count(item)}', end=" ")

