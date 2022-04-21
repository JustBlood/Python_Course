from datetime import datetime
from pkgutil import read_code
lst = [1,2,3]
print(type(repr(lst))) # Class - str
print(eval(repr(lst)) == lst) # eval opposite repr
dt = datetime.now()
print(repr(dt))
print(dt)

class Character():

    def __init__(self,race,damage = 10):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f'{self.race} with damage = {self.damage}'

    # we have eq and ne to define '==' and '!='
    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False



c = Character('Elf')
print(repr(c))
print(c)

d = eval(repr(c))
print(type(d))

# True, because we define __eq__ magic method
print(c==d)

