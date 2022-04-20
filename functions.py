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
