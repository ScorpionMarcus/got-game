import random

characters = []
dawgs = []

d = open('dawgs.txt', 'r').readlines()
c = open('characters.txt', 'r').readlines()

def removeBreak(read, arr):
    for i in read:
        arr.append(i.rstrip('\n'))

def picker():
    for i in dawgs:
        x = random.choice(characters)
        print(i + ': ' + x)
        characters.remove(x)

removeBreak(d, dawgs)
removeBreak(c, characters)
picker()