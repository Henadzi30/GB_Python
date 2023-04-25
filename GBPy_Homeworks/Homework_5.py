# Задача 26: Напишите программу, которая на вход принимает два
#  числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# num_A = int(input('Введите число A: '))
# num_B = int(input('Введите число B: '))
# def exponentiation(a, b):
#     if b == 1:
#         return a
#     while b >= 1:
#         return (a * exponentiation(a, b - 1))
    
# print(f'Результатом возведения числа {num_A} в степень {num_B} будет {exponentiation(num_A, num_B)}')


# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28 и сгенерирует ошибку, если на вход пришла
# невалидная строка.

# Пояснения: если символ встречается 1 раз, он остается без
# изменений, если символ повторяется более 1 раза, к нему
# добавляется количество повторений.

# somesing = input('>>> ')
# some_str = []
# for i in range(len(somesing)):
#     some_str.append(ord(f'{somesing[i]}'))
# print(somesing.count('B'))
# print(some_str) #65-90


def RLE(simbols):
    flag = True
    while flag:
        for i in range(len(simbols)):
            if simbols[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                flag = False
        if flag == False:
            return 'Строка введена не корректно!'
        break
    
    modified_string = []
    count_liter = 0
    for j in range(1, len(simbols)):
        if simbols[j - 1] == simbols[j]:
            count_liter += 1
        if simbols[j - 1] != simbols[j]:
            count_liter += 1
            if count_liter == 1:
                modified_string.append(simbols[j - 1])
                count_liter = 0
            elif count_liter > 1:
                modified_string.append(simbols[j - 1] + f'{count_liter}')
                count_liter = 0
            else:
                modified_string.append(simbols[j] + f'{count_liter}')
                count_liter = 0
    
    return ''.join(modified_string)       

print(RLE(input('Введите строку символов: ')))     


