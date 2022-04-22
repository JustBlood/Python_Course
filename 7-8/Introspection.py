# Intospection - is analyze data of objects
#print(issubclass.__doc__)

class Shape:
    pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

circle = Circle(10)
print(isinstance(12,int))
print(issubclass(Circle, Shape))
print(isinstance(circle, Circle),'\n')

print(callable(circle)) # object that defines __call__()
                        #is considered callable 
print(callable(print))

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius','\n'))

#print(dir(circle)) # all attributs
print(circle.__dict__,'\n') # defined us attributes

print(Circle.__name__)
print(__name__)

circle2 = circle

print(id(circle))
print(id(circle2))