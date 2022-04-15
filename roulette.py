number = int(input())
if number == 0:
    print('зеленый')
else:
    if 1 <= number <= 10:
        if number % 2 == 0:
            print('черный')
        else:
            print('красный')
    if 11 <= number <= 18:
        if number % 2 != 0:
            print('черный')
        else:
            print('красный')
    if 19 <= number <= 28:
        if number % 2 != 0:
            print('красный')
        else:
            print('черный')
    if 29 <= number <= 36:
        if number % 2 != 0:
            print('черный')
        else:
            print('красный')
    if number < 0 or number > 36:
        print('ошибка ввода')


