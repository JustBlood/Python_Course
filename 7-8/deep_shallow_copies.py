import copy

list1 = [1,2,3,[4,5,6]]

copied_list = list1.copy()
copied_list[3].append(7)

# Because obj #4 ([4,5,6]) not copied, 
# copy() just copy its link! This is shallow copy
# problems may arise with link-type objects
print(list1)
print(copied_list)

list1.append(8)
print(list1)
print(copied_list)

shallow_copy = copy.copy(list1)
shallow_copy[3].append(8)
deep_copy = copy.deepcopy(list1)
deep_copy[3].append(9)

print(shallow_copy)
print(deep_copy)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

a = Point(3,4)
b = copy.copy(a)

a.x = 5
print(b,'\n') #b was not redefine, because not-link type

class Line():

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    #redefine shallow_copy and deep_cope
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result

        for k,v in self.__dict__.items():
            setattr(result,k,copy.deepcopy(v,memo))
        return result
l1 = Line(a,b)
l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)
# But now we again have a problem with l2, because we take link on
# class Point() in class Line
print(l1.p1)
print(l2.p1)
print(l3.p1)
l1.p1.x = 4
print(l1.p1)
print(l2.p1)
print(l3.p1)