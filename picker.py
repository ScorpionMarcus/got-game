import random

# List of GoT characters
characters = [
    'Jon Snow',
    'Daenerys Targaryen',
    'Arya Stark',
    'Sansa Stark',
    'Cersei Lannister',
    'Night King',
    'Jaime Lannister',
    'Tyrion Lanniser',
    'Bran Stark',
    'Brienne of Tarth',
    'Davos Seaworth',
    'Jorah Mormon',
    'Lord Varys',
    'Euron Greyjoy',
    'Samwell Tarly',
    'Tormund Giantsbane',
    'Sandor Clegane',
    'Theon Greyjoy',
    'Gendry',
    'Gregor Clegane',
    'Beric Dondarrion',
    'Yara Greyjoy',
    'Bronn',
    'Grey Worm'
]

# Participants
dawgs = ['Squid', 'Marcus', 'Mikey', 'Gritty']

# class Player:
#     def __init__(self, name, character):
#         self.name = name
#         self.character = character

# Prints which participant gets which character
def picker():
    for i in dawgs:
        print(i + ' is assigned ' + random.choice(characters))

picker()

'''
TODO
Add player class
Assign a new character to a specific dawg after they win, without generating new characters for all dawgs
Pull characters and dawgs from csv files
'''
Remove dead character from characters
