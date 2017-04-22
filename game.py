import time
import os
from random import randint
import random
import inventory
import asciart
from enemies import *
import world

#  ex #

from character import *

character.inv.update({'Nothing' : ' ', 'Dmg' : 0, 'ARM' : 0})


os.system('clear')


def race():
    if chrace == 'h':
        character.lp += 2
        character.attk += 2
        character.arm += 3
    elif chrace == 'e':
        character.lp += 1
        character.attk += 1
        character.arm += 1
        character.mana += 2
    elif chrace == 'd':
        character.lp += 3
        character.attk += 1
        character.arm += 4
    print('So, you are one of those supercool-neckcracking-ass-kicking guys')
    print('Kewl!')
    time.sleep(3)

race()
os.system('clear')

print('_/°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\_')
print('|    Super-Kick-Ass Adventure You Shall Never Forget     |')
print('|__m_m__m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m_m___m_m__|')
print('')
print('')
print('')
print('Ascii arts from ascii.co.uk')

time.sleep(3)
os.system('clear')


world.World.City()


