from icecream import ic
s = input()
n = int(s[1::])
for i in range(n):
    sentence = input()
    if sentence.find('#') >= 0:
        x = sentence.find('#')
        print(sentence[:x].rstrip())
    else:
        print(sentence.rstrip())
