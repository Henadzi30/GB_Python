# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите число >>> '))
a = (num % 100) % 10
b = (num % 100) // 10
c = num // 100
print(f"{a + b + c} ({c} + {b} + {a})")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input("Введите количество журавликов, которое сделали Петя, Катя и Сережа: "))
piters_bierds = int(s / 6)
sergeis_bierds = int(s / 6)
katyas_bierds = 2 * (piters_bierds + sergeis_bierds)
print(piters_bierds, katyas_bierds, sergeis_bierds)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5 = 9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

num = int(input("Введите номер билета: "))

digit_1 = num // 100000
digit_2 = (num % 100000) // 10000
digit_3 = (num // 1000) % 10
digit_4 = (num // 100) % 10
digit_5 = (num // 10) % 10
digit_6 = num % 10

print(digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6)
# если вледовать условию задачи, то для соответсвующего вывода следует
if digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6:
    print('yes')
else:
    print('no')

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

n, m, k = map(int, input('Ввудите последовательно через пробел значения n, m и k: ').split())
if k < n * m and k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')



