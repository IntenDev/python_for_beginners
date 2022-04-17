from icecream import ic
s = input().split()
cnt = 0
cnt += s.count('a')
cnt += s.count('A')
cnt += s.count('an')
cnt += s.count('An')
cnt += s.count('the')
cnt += s.count('The')
print('Общее количество артиклей:', cnt)