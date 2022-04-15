# year = int(input())
# a = year % 10
# b = (year % 100) // 10
# if a == 0 and b == 0:
#     print('YES')
# else:
#     print('NO')
# ----------------------
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# sum1 = (a1 + b1) % 2
# sum2 = (a2 + b2) % 2
# if sum1 == sum2:
#     print('YES')
# else:
#     print('NO')
# ----------------------
# old = int(input())
# sex = input()
# if 10 <= old <= 15:
#     if sex == 'f':
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')
# ----------------------
# num = int(input())
# if 1 <= num <= 10:
#     if num == 1:
#         print('I')
#     elif num == 2:
#         print('II')
#     elif num == 3:
#         print('III')
#     elif num == 4:
#         print('IV')
#     elif num == 5:
#         print('V')
#     elif num == 6:
#         print('VI')
#     elif num == 7:
#         print('VII')
#     elif num == 8:
#         print('VIII')
#     elif num == 9:
#         print('IX')
#     else:
#         print('X')
# else:
#     print('ошибка')
# ----------------------
# num = int(input())
# if num % 2 != 0:
#     print('YES')
# elif 2 <= num <= 5 and num % 2 == 0:
#     print('NO')
# elif 6 <= num <=20 and num % 2 == 0:
#     print('YES')
# elif num > 20 and num % 2 == 0:
#     print('NO')
# ----------------------
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 - x2) * (y1 -y2) == 2 or (x1 - x2) * (y1 -y2) == -2:
#     print('YES')
# else:
#     print('NO')
# -----------------------
x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2 == y1 - y2) or (x1 + x2 == y1 + y2) or x1 == y1 or x2 == y2:
    print('YES')
else:
    print('NO')