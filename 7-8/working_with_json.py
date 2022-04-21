import json

class Tournament:

    def __init__(self,name,year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls,json_data):
        return cls(**json_data)


tournaments = {
    "A": 2010,
    "F": 2018,
    "FG": 2016
}

json_data = json.dumps(tournaments, indent = 2) # serialization
print(json_data)
# From str json recover dict type
loaded = json.loads(json_data) # deserialization
print(loaded)

t1 = Tournament('A',2010)
# json_data = json.dumps(t1) IS NOT JSON SERIALIZABLE
json_data = json.dumps(t1.__dict__)
print(json_data)
t = Tournament(**json.loads(json_data))
print(f'name = {t.name}, year = {t.year}\n')

class ChessPlayer:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)
t1 = Tournament("A", 2010)
t2 = Tournament("F", 2010)
t3 = Tournament("FG", 2010)

p1 = ChessPlayer([t1,t2,t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__)
print(json_data)
decoded_player = ChessPlayer.from_json(json.loads(json_data))
print(decoded_player)
print(decoded_player.tournaments,'\n')

with open("player.json", "w") as f:
    json.dump(p1,f,default=lambda obj: obj.__dict__)

with open("player.json", "r") as rf:
    data = json.load(rf)
print(data)
decoded_player = ChessPlayer.from_json(data)
print(decoded_player)
print(decoded_player.tournaments)