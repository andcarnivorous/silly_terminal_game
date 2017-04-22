from character import *
import world
from enemies import *
import inventory
import os

def init(enmy):
    print(character.name, 'HP: ', character.lp)
    print(enmy.name, 'HP: ', enmy.lp)
    while True:

        print('What do you want to do?')

        if chrace == 'h':
            print('[Attack (a)]     [Piss yourself & run (p)]')
        elif chrace == 'd':
            print('[Attack (a)]     [Piss yourself & run (p)]')
        elif character.mana > 0:
            print('[Attack (a)]     [Magick Attack (m)]     [Piss yourself & run (p)]')
        else:
            print('[Attack (a)]     [OUT OF MANA!]     [Piss yourself & run (p)]')

        print('Your Basic Damage is ', character.attk + character.inv['Dmg'])
        startcombat = input('>>>>')

        if startcombat == 'a':
            enemy.Combat(enmy)
        elif startcombat == 'm' and character.mana > 0:
            enemy.MagicCombat(enmy)
            character.mana -= 1
        elif startcombat == 'p':
            print('Bye!')
            world.World.City()
        else:
            print('YOU ARE OUT OF MANA!')
            pass

        if character.lp == 0 or character.lp <= 0:
            print('You lost!')
            quit()
        elif enmy.lp == 0 or enmy.lp <= 0:
            os.system('clear')
            print('You won!')
            prize = random.randint(5, 10)
            character.money += prize
            print('You won', prize, 'golds. You now have', character.money, 'golds.')
            character.lp = 20
            if chrace == 'h':
                character.lp += 2
            elif chrace == 'e':
                character.lp += 1
            elif chrace == 'd':
                character.lp = + 3

            character.keys.append(enmy.keys)

            print('You found this object:')
            objprize = random.choice(inventory.items)
            print(objprize)
            answ = input('do you want it?')
            if answ == 'y':
                character.inv.clear()
                character.inv.update(objprize)

                print(character.inv)
                print(character.attk, character.lp)
                os.system('clear')
                if character.loc == {'Tavern': 1}:
                    world.World.Tavern()

                elif character.loc == {'Harbor' : 2}:
                    world.World.Harbor()

                elif character.loc == {'Market' : 3}:
                    world.World.Market()

                elif character.loc == {'Brothel' : 4}:
                    world.World.Brothel()

                else:
                    world.World.City()
            else:
                if character.loc == {'Tavern': 1}:
                    world.World.Tavern()

                elif character.loc == {'Harbor' : 2}:
                    world.World.Harbor()

                elif character.loc == {'Market' : 3}:
                    world.World.Market()

                elif character.loc == {'Brothel' : 4}:
                    world.World.Brothel()

                else:
                    world.World.City()

        else:

            pass

