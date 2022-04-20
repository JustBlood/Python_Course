class Player():
    MAX_SPEED = 100
    death_health = 0

    def __init__(self, race, damage=10):
        self.__race = race
        self.damage = damage
        self._health = 100
        self._current_speed = 20
        print('Player created')

    def hit(self, damage):
        self._health -= damage
    
    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed
    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    def is_dead(self):
        return self._health <= Player.death_health

unit = Player('Elf')

# Change private atributs
# unit._Player__race = 'Ork'
# print(unit._Player__race)

print(unit.health)
print(unit.race)

# decorator property + setter (to post value)
unit.current_speed = 120
print(unit.current_speed)
unit.current_speed = -999
print(unit.current_speed)