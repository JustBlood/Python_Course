import random
import itertools


def randoms(min,max,n):
#    return [random.randint(min,max) for _ in range(n)] - with List()
    for _ in range(n):
        yield random.randint(min,max) #lazy evaluation with generator

for r in randoms(10,30,5):
    print(r)

rand_sequence = randoms(1,10,10)
print('\n',rand_sequence)
for r in rand_sequence:
    print(r)
print('===')
for r in rand_sequence:
    print(r)


def randoms2(min,max):
    while True:
        yield random.randint(min,max)

rand_sequence = randoms2(1,100000)
five_taken = list(itertools.islice(rand_sequence, 5))
print('\n',five_taken)


# lazy reading:

def read_line_by_line(file):
    """Lazy function (generator) to read a file line be line"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line

file = open(r'E:\prog_py\Course_py\0. myDecisions\7-8\test.txt')
for line in read_line_by_line(file):
    print(line.strip().capitalize())
"""next() function:

rand_seq = randoms2(1,10)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
"""

my_list = [1,2,3,4]
squares = [x**2 for x in my_list]
print('\n',squares)
squares1 = (x**2 for x in iter(my_list))
print(squares1)
for i in squares1:
    print(i)