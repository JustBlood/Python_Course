class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point x = {self.x}, y = {self.y}'

p = Point(3,4)
print(p)

class Road():
    def __init__(self,length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f'A road of length: {self.length}'

    def __del__(self):
        print('The road has been destroyed')

r = Road(100)
print(len(r))
print(r)