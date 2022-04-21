from abc import ABC
from abc import abstractmethod
import math

class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print('Calc perimeter')
        pass

    def drag(self):
        print('Basic dragging functionality')

# Abstract class can't be created as param
# s = Shape() - ERROR

# We should redefine  ALL abstracts methods in subclasses from abstract_class
class Triangle(Shape):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'Drawing triange with sides {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.perimeter())/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(10,10,10)
print(triangle.area(), triangle.drag())