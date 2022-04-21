from secrets import choice
from numpy import transpose

class TikTak:
    def __init__(self, args):
        print("Game start! All sections are empty.\n")
        self.args = args
    
    def addArgs(self, new_args):
        self.args = new_args

    def win_check(self):
        for i in self.args:
            if i[0]==i[1]==i[2] != "_": return True
        for i in transpose(self.args):
            if i[0]==i[1]==i[2] != "_": return True
        if self.args[0][0] == self.args[1][1] == self.args[2][2] != "_": return True
        if self.args[0][2] == self.args[1][1] == self.args[2][0] != "_": return True
        return False


    def draw(self):
        print(' _ _ _ ')
        print(f"|{self.args[0][0]}|{self.args[0][1]}|{self.args[0][2]}|")
        print(f"|{self.args[1][0]}|{self.args[1][1]}|{self.args[1][2]}|")
        print(f"|{self.args[2][0]}|{self.args[2][1]}|{self.args[2][2]}|")
        print(' _ _ _ ')
            
def check_corr_input(choice):
    if choice < 3:
        if now_arguments[0][choice] == '_':
            return True
        else: print("This cell isn't empty now! Try another.\n")
    elif choice < 6:
        if now_arguments[1][choice-3] == '_':
            return True
        else: print("This cell isn't empty now! Try another.\n")
    elif choice < 9:
        if now_arguments[2][choice-6] == '_':
            return True
        else: print("This cell isn't empty now! Try another.\n")
    else: print("This cell isn't exist! Try another.\n")
    return False

print("Hello, my friend! Let's start\n")
now_arguments = [['_']*3,['_']*3,['_']*3]
c = TikTak(now_arguments)
c.draw()
while True:
    while True:
        choice1 = int(input("Please, the first player, give me your cell choice: "))
        if check_corr_input(choice1): break
    if choice1 < 3: now_arguments[0][choice1] = 'X'
    elif choice1 < 6: now_arguments[1][choice1-3] = 'X'
    else: now_arguments[2][choice1-6] = 'X'
    
    
    c.draw()

    if c.win_check():
        print('Congratulations! First player win.\n')
        break
    
    while True:
        choice2 = int(input("Please, the second player, give me your cell choice: "))
        if check_corr_input(choice2): break
    if choice2 < 3: now_arguments[0][choice2] = '0'
    elif choice2 < 6: now_arguments[1][choice2-3] = '0'
    else: now_arguments[2][choice2-6] = '0'
    
    c.draw()
    if c.win_check():
        print('Congratulations! Second player win.\n')
        break
