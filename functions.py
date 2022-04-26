from icecream import ic
from math import pi
# объявление функции
# def draw_box():
#     for i in range(1, 14):
#         if i == 1 or i == 13:
#             print('*' * 10, end='')
#             print()
#         if i != 13:
#             print('*' + (' ' * 8) + '*')
# # основная программа
# draw_box()  # вызов функции
# -----------------------------
# объявление функции
# def draw_triangle():
#         for i in range(1, 11):
#             print(('*') * i)
#
# # основная программа
# draw_triangle()  # вызов функции
# ------------------------------

# объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, (base // 2) + 2):
#         print(fill * i)
#     for j in range(base // 2, 0, -1):
#         print(fill * j)
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)
# -------------------------------
# объявление функции
# def print_fio(name, surname, patronymic):
#     fio = []
#     fio.append(surname[0].upper())
#     fio.append(name[0].upper())
#     fio.append(patronymic[0].upper())
#     print(*fio, sep='', end='')
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)
# --------------------------------
# объявление функции
# def print_digit_sum(num):
#     n = 0
#     for i in str(num):
#         n += int(i)
#     print(n)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)
# flag = True
# sentence = []
# while flag:
#     s = input()
#     if s == '':
#         flag = False
#     else:
#         sentence.append(s)
# print(sentence)
# -------------------------------
# объявление функции
# def get_days(month):
#     if month == 2:
#         return 28
#     if month % 2 != 0 and month <= 7:
#         return 31
#     elif month % 2 != 0 and month > 7:
#         return 30
#     if month % 2 == 0 and month <= 7:
#         return 30
#     elif month % 2 == 0 and month > 7:
#         return 31
#
# считываем данные
# num = int(input())

# вызываем функцию
# print(get_days(num))
# -----------------------------
# объявление функции
# def get_factors(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     return count
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))
# -------------------------
# объявление функции
# def find_all(target, symbol):
#     myList = []
#     for i in range(len(target)):
#         if symbol == target[i]:
#             myList.append(i)
#     return myList
#
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))
# -----------------------------
# объявление функции
# def merge(list1, list2):
#     myList = list(list1 + list2)
#     myList.sort()
#     return myList
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# вызываем функцию
# print(merge(numbers1, numbers2))

# ------------------------------
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#
#     return result
#
# myList = []
# n = int(input())
# for i in range(n):
#     list_input = input().split()
#     for i in range(len(list_input)):
#         list_input[i] = int(list_input[i])
#     myList = quick_merge(list_input, myList)
# print(*myList)
# -----------------------------------
# объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if side1 > 0 and side2 > 0 and side3 > 0:
#         if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))
# Проверка на простоту числа
# объявление функции
# def is_prime(num):
#     flag = True
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))
# ------------------------------
# def is_prime(num):
#     flag = True
#
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
# def get_next_prime(num):
#     flag1 = False
#     count = num + 1
#     while not flag1:
#         if is_prime(count):
#             flag1 = True
#             return count
#         else:
#             count += 1
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))
# --------------------------------
# Good password
# объявление функции


# def is_password_good(password):
#     flag = True
#     if len(password) < 8:
#         flag = False
#     if password == password.lower():
#         flag = False
#
#     if password == password.upper():
#         flag = False
#
#     if not [i for i in password if i in '0123456789']:
#         flag = False
#     return flag
#
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_password_good(txt))
# --------------------------------

# объявление функции
# def is_one_away(word1, word2):
#     flag = False
#     cnt = 0
#     if len(word1) == len(word2):
#       flag = True
#     for i in range(len(word1.lower())):
#       if word1[i] == word2.lower()[i]:
#         continue
#       else:
#         cnt += 1
#     if 0 == cnt or cnt > 1:
#       flag = False
#     return flag
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

# Палиндром

# объявление функции
# def is_palindrome(text):
#     txt1 = ''.join(c.lower() for c in text if c.isalpha())
#     if txt1 == txt1[::-1]:
#         return True
#     else:
#         return False
# # считываем данные
# txt = input()
#
#
# # вызываем функцию
# print(is_palindrome(txt))
# -----------------------------

# объявление функции
# def is_valid_password(password):
#     password = password.split(':')
#     flag_len = False
#     flag_a = False
#     flag_b = False
#     flag_c = False
#     if len(password) == 3:
#         flag_len = True
#     if password[0] == password[0][::-1]:
#         flag_a = True
#     d = 2
#     while int(password[1]) % d != 0:
#         d += 1
#     flag_b = d == int(password[1])
#     if int(password[2]) % 2 == 0:
#         flag_c = True
#
#     if flag_len == flag_a and flag_a == flag_b and flag_b == flag_c:
#         return True
#     else:
#         return False
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))
# ---------------------------------
# объявление функции
# def is_correct_bracket(text):
#     cnt = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             cnt += 1
#         elif text[i] == ')':
#             cnt -= 1
#         if cnt < 0:
#             break
#     if cnt == 0:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))
# ------------------------------
# From CamelCase to snake_case
# объявление функции
# def convert_to_python_case(text):
#     text1 = list(text)
#     for i in range(len(text1)):
#         if text1[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#
#             if i == 0:
#                 text1[i] = text1[i].lower()
#
#             if i > 0:
#                 text1.insert(i, '_')
#                 text1[i+1] = text1[i+1].lower()
#     result = ''.join(text1)
#     return result
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))
# -----------------------------
# Вычисление середины отрезка по координатам

# объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     a = (x1 + x2) / 2
#     b = (y1 + y2) / 2
#     return a, b
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)
# ------------------------------
# Площадь и длина
# from math import pi
# # объявление функции
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * (radius ** 2)
#     return c, s
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)
# -------------------------------
# Корни уравнения
# from math import *
# # объявление функции
# def solve(a, b, c):
#     d = (b ** 2) - (4 * a * c)
#     if d == 0:
#         return -b / (2 * a), -b / (2 * a)
#     else:
#         x1 = (-b + sqrt(d)) / (2 * a)
#         x2 = (-b - sqrt(d)) / (2 * a)
#         if x1 > x2:
#             return x2, x1
#         else:
#             return x1, x2
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)
# ---------------
# ЭКЗАМЕН ПО ФУНКЦИЯМ
# ---------------
# Задача: Ëлочка
# объявление функции
#
# ---------------
# Задача: Калькулятор доставки

# объявление функции
# def get_shipping_cost(quantity):
#     return 1000 + (120 * (quantity - 1))
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))
# ------------------
# Задача: Биномиальный коэффициент
# from math import *
# # объявление функции
# def compute_binom(n, k):
#     return int(factorial(n) // (factorial(k) * factorial(n-k)))
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))
# ------------------
# # Задача: Число словами
# # объявление функции
# def number_to_words(num):
#     num1 = str(num)
#     num_up_to_10 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     num_from_10_to_19 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     num_from_20 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if len(num1) == 1:
#         return num_up_to_10[num]
#     elif 9 < num < 20:
#         return num_from_10_to_19[num % 10]
#
#     elif num >= 20:
#         if num % 10 == 0:
#             return num_from_20[(num // 10) - 2]
#         else:
#             return num_from_20[(num // 10) - 2] + ' ' + num_up_to_10[num % 10]
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))
# ----------------------------
# Задача: Искомый месяц
# объявление функции
# def get_month(language, number):
#     rus = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == 'ru':
#         return rus[number - 1]
#     else:
#         return eng[number -1]
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))
# ---------------------
# Задача: Магические даты
# объявление функции
# def is_magic(date):
#     date = date.split('.')
#     return int(date[0]) * int(date[1]) == int(date[2]) % 100
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))
# ----------------------
# Задача: Панаграммы
# объявление функции
# def is_pangram(text):
#     text1 = ''.join(text.split(' ')).lower()
#     cnt = []
#     for i in range(len(text1)):
#         if text1[i] in 'abcdefghijklmnopqrstuvwxyz' and text1[i] not in cnt:
#             cnt.append(text1[i])
#     if len(cnt) == 26:
#         return True
#     else:
#         return False
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))
