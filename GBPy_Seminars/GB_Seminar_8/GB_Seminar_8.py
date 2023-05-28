# with open('baza.txt', 'r', encoding='utf-8') as file:
#     file.seek(0)
#     text = file.read()
#     print(text)

    
# with open('baza.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('baza.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         print(letter)
        
# with open('baza.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines()) # построчно считывает и формирует список, не видны переносы '\n'

# with open('baza.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines() # показывает в массиве знаки '\n'
#     print(text)

# with open('baza.txt', 'w', encoding='utf-8') as file:
#     some_list = ['hello', 'world', 'how', 'are', 'you']
#     for el in some_list:
#         file.write(el + '\n')

# import json
# some_dict = {1: 2, 2: 3}
# with open('example.json', 'w', encoding='utf-8') as file:
#     json.dump(some_dict, file)


# with open('example.json', 'w', encoding='utf-8') as file:
#     some_dict = {1: 2, 2: 3}
#     file.write(str(some_dict)[1: -1])

# Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый 
# текстовый файл все эти строки.

# Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле.

# with open('practic.txt', 'w', encoding='utf-8') as file:
#     count_row = int(input('Введите количество требуемых строк: '))
#     for i in range(count_row):
#         strok = input('Введите строку: ')
#         file.write(strok + '\n')

# with open('practic.txt', 'r', encoding='utf-8') as file:
#     find_simbol = input('Введите символ(букву), количество вхождений которой необходимо найти: ')
#     count_simbol = 0
#     while True:        
#         line = file.readline()        
#         if not line:
#             break
#         for i in range(len(line)):
#             if find_simbol == line[i]:
#                 count_simbol += 1
#     print(count_simbol)



# Напишите функцию read_last(lines, file), которая будет открывать определенный файл
# file и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное число).
# Протестируем функцию на файле "article.txt" со следующим содержимым:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# with open('article.txt', 'w', encoding='utf-8') as file:
#     task_list = ['Вечерело', 'Жужжали мухи', 'Светил фонарик', 'Кипела вода в чайнике', 'Венера зажглась на небе', 'Деревья шумели',
#                  'Тучи разошлись', 'Листва зеленела']
#     for el in task_list:
#         file.write(el + '\n')

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.read()
#         sm_list = text.splitlines() # построчно считывает и формирует список, не видны переносы '\n'
#         while True:
#             if lines <= 0:
#                 break
#             for elem in range(len(sm_list)):
#                 if elem >= len(sm_list) - lines:
#                     print(sm_list[elem])
#             break
    
# read_last(5, 'article.txt')


# Документ "article.txt" содержит следующий текст:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, 
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().replace('\n', ' ')
        txt_list = text.split(' ')
        max_wrld = []
        max_len = 0
        for el in range(len(txt_list)):
            if len(txt_list[el]) > max_len:
                max_len = len(txt_list[el])
        for elem in range(len(txt_list)):
            if len(txt_list[elem]) == max_len:
                max_wrld.append(txt_list[elem])
    return max_wrld
            

print(* longest_words('article.txt'))


# Задача №49. 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые
# должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной