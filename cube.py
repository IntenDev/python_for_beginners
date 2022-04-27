import random
import os
again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики...')
    os.system('say "Бросаем кубики"')
    print('Значение граней: ')
    print(random.randint(1,6))
    print(random.randint(1,6))
    os.system('say "Бросить кубики еще раз?"')
    again = input('Бросить кубики еще раз? (д, н) ')
    os.system('afplay /System/Library/Sounds/Sosumi.aiff')
os.system('say "Ваша программа закончена"')

