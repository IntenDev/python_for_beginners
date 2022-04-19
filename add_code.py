keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i[1:] for i in keywords]
# print(new_keywords)
# ------------------
# lengths = [len(i) for i in keywords]
# print(lengths)
# ------------------
# new_keywords = [i for i in keywords if len(i) >= 5]
# print(new_keywords)
# ------------------
# palindromes = [i for i in range(100, 1000) if str(i)[0] == str(i)[2]]
# print(palindromes)
# ------------------
# n = int(input())
# square = [ i ** 2 for i in range(1, n + 1)]
# print(*square, sep='\n')
# -------------------
# n = input().split()
# square = [int(i) ** 3 for i in n]
# print(*square)
# -------------------
# print(*[i for i in input().split()], sep='\n')
# -------------------
# print(*[i for i in input() if i.isdigit()], sep='')
# -------------------
print(*[int(i) ** 2 for i in input().split() if (int(i) % 2) == 0 and (int(i) ** 2) % 10 != 4])
