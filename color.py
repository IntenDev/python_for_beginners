color1, color2 = input(), input()

if color1 != 'красный' and color1 != 'синий' and color1 != 'желтый' or color2 != 'красный' and color1 != 'синий' and color1 != 'желтый':
    print('ошибка цвета')
else:
    if color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
        print('оранжевый')
    elif color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
        print('фиолетовый')
    elif color1 == 'желтый' and color2 == 'синий' or color1 == 'синий' and color2 == 'желтый':
        print('зеленый')
    elif color1 == 'красный' and color2 == 'красный':
        print('красный')
    elif color1 == 'желтый' and color2 == 'желтый':
        print('желтый')
    elif color1 == 'синий' and color2 == 'синий':
        print('синий')
