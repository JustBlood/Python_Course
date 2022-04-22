import pickle

class Character():
    # to reading out of file specially:
    def __setstate__(self,state):
        self.race = state.get('race','Elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)

    #def __getstate__(self): -> to writing in file specially

    def __init__(self, race, armor, damage = 10):
        self.race = race
        self.damage = damage
        self.health = 100
        self.armor = armor

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

c = Character('Elf', 100)
c.hit(10)
print(c.health)

with open('game_state.bin', 'w+b') as f:
    pickle.dump(c, f)

# Deliting our obj
c = None
# Read our object from saved pick in file game_state
with open('game_state.bin', 'rb') as f:
    c = pickle.load(f)
print(c.health)
print(c.__dict__)