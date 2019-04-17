import random
import datetime

characters = []
dawgs = []

d = open('dawgs.txt', 'r').readlines()
c = open('characters.txt', 'r').readlines()
w = open('logs.txt', 'a')

def removeBreak(read, arr):
    for i in read:
        arr.append(i.rstrip('\n'))

def picker():
    for i in dawgs:
        x = random.choice(characters)
        print(i + ': ' + x)
        w.write(i + ': ' + x + '\n')
        characters.remove(x)

removeBreak(d, dawgs)
removeBreak(c, characters)
w.write(str(datetime.datetime.now()) + '\n')
picker()
w.write('\n')