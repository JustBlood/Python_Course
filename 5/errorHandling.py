import math

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as ex:
        print(f'an error occured: {ex}')
    except:
        print('unknown error occured!')

def calc_square(ab,ac,bc):
    if ab<=0 or ac<=0 or bc<=0:
        # Standart raise
        #raise ValueError("One of the sides is less or equal to 0.")
        
        #Custom raise
        raise InvalidTriangleError("One of the sides is less or equal to 0.")
    p = (ab+ac+bc)/2
    s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    return s

# def custom exception
class InvalidTriangleError(Exception):
    '''Raised when a triangle has invalid sides'''

#handling error in func
print(divide(6,0),'\n')

#try finally and else
file = None
try:
    file = open(r'C:\tmp\abrecadabra.txt')
    data = file.read()
except FileNotFoundError as ex:
    print(f'Error has occured. Description: {ex.strerror}')
else:
    print('maybe else')
finally:
    print('Finally')
    if file:
        file.close()

#
square = calc_square(10,10,10)
print(square)
# Non valid result, but not an error. This is bug
try:
    square = calc_square(2,8,8)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(square)
