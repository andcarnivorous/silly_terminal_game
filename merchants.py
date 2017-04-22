from character import *
import world
import time
import os

def TavernOwner():
    print('"Well hello there nice traveler! You look quite tired, depressed and filled with the void of existance!')
    print('Nothing will fit you better than a nice hot piss-like pint of ale!\n What do you say? Shall I pour you one?"')
    print('[Yes, please let me drown my sorrows in cheap booze (y)]     [No, thanks (n)]')
    answ = input('>>>> ')
    if answ == 'y':
        if character.money >= 5:
            character.money -= 5
            print('"Thanks! Please notice the strong aroma of old rotting wood accompanied by a soft note of personal urine!"')
            print('You paid 5\n You now have', character.money, 'golds')
            time.sleep(3)
            os.system('clear')
            world.World.Tavern()
        elif character.money < 5:
            print('"Sorry, no bums in here.\n Please do come back when you have a less miserable life and some golds"')
            time.sleep(3)
            os.system('clear')
            world.World.City()
        else:
            pass
    else:
        print('"Ok, do not worry my friend!\n Please, do come back when you feel more like a man and less like a pussy."')
        time.sleep(3)
        os.system('clear')
        world.World.Tavern()

def MarketMerchant():
    print('"Well hello there nice traveler! You look quite tired, depressed and filled with the void of existance!')
    print('Nothing will fit you better than a nice hot piss-like pint of ale!\n What do you say? Shall I pour you one?"')
    print('[Yes, please let me drown my sorrows in cheap booze (y)]     [No, thanks (n)]')
    answ = input('>>>> ')
    if answ == 'y':
        if character.money >= 5:
            character.money -= 5
            print('"Thanks! Please notice the strong aroma of old rotting wood accompanied by a soft note of personal urine!"')
            print('You paid 5\n You now have', character.money, 'golds')
            time.sleep(3)
            os.system('clear')
            world.World.Tavern()
        elif character.money < 5:
            print('"Sorry, no bums in here.\n Please do come back when you have a less miserable life and some golds"')
            time.sleep(3)
            os.system('clear')
            world.World.City()
        else:
            pass
    else:
        print('"Ok, do not worry my friend!\n Please, do come back when you feel more like a man and less like a pussy."')
        time.sleep(3)
        os.system('clear')
        world.World.Tavern()

    pass