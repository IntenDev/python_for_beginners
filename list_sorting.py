from icecream import ic
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)
# for i in range(n):
#     smallest = i
#     for j in range(i + 1, n):
#         if a[j] < a[smallest]:
#             smallest = j
#     a[i], a[smallest] = a[smallest], a[i]
# print(a)

# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# for i in range(1, len(a)):
#     for j in range(i):
#         if a[j] >= a[i]:
#             a[i], a[j] = a[j], a[i]
# print(a)
# [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]
# for i in range(1, len(a)):
#     element = a[i]
#     j = i - 1
#     while j >= 0 and a[j] > element:
#         a[j + 1] = a[j]
#         j -= 1
#         a[j + 1] = element

# print(a)
# ЭКЗАМЕН --------------------------------
#
# a, b = input().split(), input().split()
# L = list([int(a[x]) for x in range(len(a))])
# M = list([int(b[y]) for y in range(len(b))])
# sum_LM = list([L[i] + M[i] for i in range(len(L))])
# print(*sum_LM)

# s = input().split()
# m = [s[0]]
# z = 0
# for i in range(1, len(s)):
#     m.append('+')
#     m.append(s[i])
#     z += int(s[i])
# result = ''.join(m)
#
# print(result + '=', z + int(m[0]), sep='')
# s = input().split('-')
# flag = True
# num = len(s[-1])
# if len(s) < 3:
#     flag = False
# if len(s) == 4 and s[0] == '7':
#     for i in range(1, len(s) - 1):
#         if not s[i].isdigit() or not s[-1].isdigit():
#             flag = False
#             break
#         if len(s[i]) == 3 and num == 4:
#             continue
#         else:
#             flag = False
#             break
#
# elif len(s) == 3:
#     for i in range(len(s) - 1):
#         if not s[i].isdigit() or not s[-1].isdigit():
#             flag = False
#             break
#         if len(s[i]) == 3 and num == 4:
#             continue
#         else:
#             flag = False
#             break
# else:
#     flag = False
# if flag:
#     print('YES')
# else:
#     print('NO')
#s = [len(i) for i in input().split()]
# print(max([len(i) for i in input().split()]))
# s = input().split()
# print(*[i[1:] + i[:1] + 'ки' for i in input().split()])