from typing import Callable
import random

ALP = '''ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'''


class Game:
    def __init__(self, mistakes_max: int):
        self._entered_letters = ''
        self.__list_of_words = []
        self.__mistakes_max = mistakes_max
        self.__mistakes_counter = 0
        self.__end_of_game_event = 0
        self.__game_status = ''
        self.__fill_in_words(self.__list_of_words)
        self.__new_word = ''
        self.__create_new_word()
        print('Game started!')

    def __fill_in_words(self, list_of_words):
        with open('words.txt', encoding='utf8') as file:
            for line in file:
                line = line.replace('\n', '')
                list_of_words.append(line)

    def check_game_status(self):
        return f'{self.__game_status}. All entered letters = {self._entered_letters}'

    def __create_new_word(self):
        self.__new_word = random.choice(self.__list_of_words)
        print(self.__new_word)
        for _ in range(len(self.__new_word)):
            self.__game_status += '*'
        return 'Successful!'

    def give_letter(self, letter: str):
        if letter in self.__new_word:
            self._entered_letters += letter
            for i in range(len(self.__game_status)):
                if self.__new_word[i] == letter:
                    self.__game_status = self.__game_status[:i] + letter + self.__game_status[i + 1:]
            return 'You guessed it! Letter has been added to word.'
        else:
            self._entered_letters += letter
            self.__mistakes_counter += 1
            return 'This letter is not in the guessed word'

    def game_status(self):
        if self.__game_status == self.__new_word:
            print('You won! Congrats!')
            while True:
                inp = input('Do you wanna play again? 1/0:\n')
                if inp == '1':
                    return 1
                elif inp == '0':
                    return 0
                else:
                    continue
        elif self.__mistakes_counter > self.__mistakes_max:
            print('You lose.')
            while True:
                inp = input('Do you wanna play again? 1/0:\n')
                if inp == '1':
                    return 1
                elif inp == '0':
                    return 0
                else:
                    continue
        else:
            return 2


print("Hello! Let's start the game!")
while True:
    while True:
        try:
            mistakes = int(input('Enter count of mistakes you want: '))
        except:
            print('Enter a NUMBER!')
        break
    game = Game(mistakes)
    while True:
        try:
            action = int(input("Enter '1' - to check game status. Enter '2' - to enter letter: "))
        except:
            print('Enter a number, please.')
            continue
        if action == 1:
            print(game.check_game_status())
        else:
            while True:
                letter = input('Enter a letter: ')
                if len(letter) == 1 and letter not in game._entered_letters and letter in ALP:
                    print(game.give_letter(letter))
                    break
                print('Incorrect input. Letter not in Russian alphabet or has already been introduced. Try another.')
        a = game.game_status()
        if a == 1:
            del game
            break
        elif a == 0:
            print('Thanks for playing! Bye.')
            exit()