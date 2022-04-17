from icecream import ic
num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
num_copy = num.copy()
num_copy[num.index(max(num))] = num[num.index(min(num))]
num_copy[num.index(min(num))] = num[num.index(max(num))]
print(*num_copy)
