while True:
    try:
        nowSticks = int(input('Введите кол-во палочек для игры: '))
    except:
        print('Введите число, а не строку.')
        continue

    while nowSticks > 0:
        while True:
            first = 0
            try:
                first = int(input(('Игрок №1, в куче {} палочек.\n\
Возьмите от 1 до 3 палочек. \n\tВведите число забираемых палочек: '.format(nowSticks))))
            except:
                print('Неверный ввод! Вы должны ввести ЧИСЛО от 1 до 3\n')
                continue

            if 0 > first > 4: print('Неверный ввод! Вы должны ввести ЧИСЛО от 1 до 3\n')
            else:
                nowSticks -= int(first)
                break
        if nowSticks <= 0:
            print('Первый игрок проиграл! Палочки закончились.\n')
            break
        while True:
            second = 0
            try:
                second = int(input(('Игрок №2, в куче {} палочек.\n\
Возьмите от 1 до 3 палочек. \n\tВведите число забираемых палочек: '.format(nowSticks))))
            except:
                print('Неверный ввод! Вы должны ввести ЧИСЛО от 1 до 3\n')
                continue

            if 0 > first > 4: print('Неверный ввод! Вы должны ввести ЧИСЛО от 1 до 3\n')
            else:
                nowSticks -= second
                break
        if nowSticks <= 0:
            print('Второй игрок проиграл! Палочки закончились.\n')
            break

    keepOn = int(input('Продолжить игру? 1 - да. 0 - нет: '))
    if keepOn == 0:
        break
print('Спасибо за игру!')
