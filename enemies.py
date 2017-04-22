from character import *
import random
from random import randint
import asciart


class enemy:
    def __init__(self, name, lp, attk, keys):
        self.name = name
        self.lp = lp
        self.attk = attk
        self.keys = keys

    def Combat(self):
        print(random.choice([asciart.FightArt, asciart.FightArt2]))
        print(random.choice(asciart.randsent))
        character.lp -= (self.attk - character.arm + randint(1, 4))
        print('You have', character.lp, 'HP left')
        self.lp -= character.attk + character.inv['Dmg'] + randint(1, 4)
        print(self.name, 'has', self.lp, 'HP left')

    def MagicCombat(self):
        print(random.choice([asciart.FightArt, asciart.FightArt2]))
        print(random.choice(asciart.randsent))
        character.lp -= (self.attk - character.arm + randint(1, 4))
        print('You have', character.lp, 'HP left')
        self.lp -= character.attk + character.inv['Dmg'] + randint(1,
                                                                   4) + character.mana + character.attk + character.arm
        print(self.name, 'has', self.lp, 'HP left')


class Orc(enemy):
    pass


glu = Orc('GluGlu', 15, 3, 'Pizza')


class Goblin(enemy):
    pass


mongl = Goblin('Mongl', 12, 2, 'Dough')


class Hum(enemy):
    pass


thief = Hum('Rat', 10, 4, 'Tea')


class Drag(enemy):
    pass

boss = Drag('Gulo', 30, 6, 'Win')
