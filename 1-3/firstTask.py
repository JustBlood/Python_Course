import random
while True:
    #Задуманное число
    thinkedNum = random.randint(1,50)
    print('''Начало игры!\n
    Вы должны угадать случайно сгенерированное число от 1 до 50!
    Вам даётся всего 6 попыток. Действуйте с умом или полагайтесь на удачу!\n''')
    #счетчик и обозначитель победы
    i = 1
    win = 0
    while i<7:
        #Введенное число
        enteredNum = int(input('У вас осталось {} попыток. Введите число: '.format(7-i)))
        #Обработка введенного числа
        if enteredNum > thinkedNum:
            print('Увы, неверно! Это число больше, чем загаданное.')
        if enteredNum < thinkedNum:
            print('Увы, неверно! Это число меньше, чем загаданное.')
        else:
            print('Невероятно! Вы угадали! Поздравляем!')
            win = 1
            break
        i+=1
    #Концовки игры
    if win==0:
        print('Увы, попытки закончились...\n\
            Чтобы начать игру заново - нажмите 1.\n\
            Чтобы выйти, нажмите 0.')
    else:
        print('Победа, победа, время обеда.\n\
            Чтобы начать игру заново - нажмите 1.\n\
            Чтобы выйти, нажмите 0.')
    keepOn = int(input())
    if keepOn == 0:
        break
print('\n Спасибо за игру!')