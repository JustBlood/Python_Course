import itertools as it


#print(dir(it)) #all methods of itertools

even_numbers = [x for x in range(10) if x%2==0]
print(even_numbers)
even_numbers1 = it.count(0,2)
print(even_numbers1)

#for x in even_numbers1: -> endless stream of numbers
#    print(x)

print(list(next(even_numbers1) for _ in range(5)))
print(list(zip(it.count(), ['a','b','c'])))

def print_iterable(iterable,end=None):
    for x in iterable:
        if end:
            print(x,end=end)
        else:
            print(x)

ones = it.repeat(1,5)
print_iterable(ones,' ')

print('\n',list(map(pow, range(10), it.repeat(2))),'\n')

# for _ in it.repeat(None,10000): -. faster than default for...range():
#     # do something

# for _ in range(10000):
#     # compute

# it.cycle()
pos_neg_ones = it.cycle(['A','B','C'])
print(list(next(pos_neg_ones) for _ in range(5)),'\n')

#it.accumulate()
print(list(it.accumulate([1,4,3,2,2,2,2,5,7,9,8,7,4,1,0],max)),'\n')

#it.chain() and it.chain_from_iterable
print(list(it.chain('ABC','DEF')))
print(list(it.chain.from_iterable(['ABC','DEF'])),'\n')

#it.dropwhile() and it.takewhile() and it.filterfalse()
print(list(it.dropwhile(lambda x: x<3, [1,2,3,4,5])))
print(list(it.takewhile(lambda x: x<3, [1,2,3,4,5])))
print(list(it.filterfalse(lambda x: x%2==0, range(10))))

iterable = iter([1,2,3])
print_iterable(iterable,' ')