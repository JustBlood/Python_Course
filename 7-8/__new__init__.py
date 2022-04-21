# __new__ doing allocation data in memory
# After __new__ implemented __init__, which initializing object
class Character:
    
    def __new__(cls):
        obj = super().__new__(cls)
        return obj

    def __init__(self):
        self.race = 'Elf'

class Character1:
    
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'

c = Character1()
c1 = Character1()
print(c1._instance)