from icecream import ic
import re
n = int(input())
negatives = []
zeros = []
positives = []
for _ in range(n):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)
print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')