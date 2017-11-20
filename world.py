import os
from character import *
from enemies import *
from combat import *
import merchants
import time

bosskeys = [glu.keys, mongl.keys, thief.keys]

def stats():

    print('_________________________')
    print('Basic Attack : ', character.attk)
    print('Basic Armor  : ', character.arm)
    print('Basic Mana   : ', character.mana)
    print('Weapon       : ', charinv.wpnname, ":", charinv.itemdmg)
    print('Amor         : ', charinv.armname, ":", charinv.itemarm)
    print('Jewel        : ', charinv.jwlname, ":", charinv.itemmana)    
    print('Money        : ', character.money)
    print('_________________________')
    destination = input('>>>')
    if destination == 'a':
        os.system('clear')
        World.City()
    else:
        World.City()
 
class World:

    def City():
        if all((key in character.keys for key in bosskeys)):
            World.Boss()
        else:
            print(asciart.city)
            print(character.keys)
            print('You are in a misterious but yet familiar city. There are old buildings from the middle age or something,')
            print('drunk men in the narrow streets and stressed out women who probably make 10c on the $ compared to those men.')
            print('This is what the town looks like (nice shithole, huh?):')
            print('Where do you go?')
            print('[Tavern (a)]       [Harbor (b)]      [Brothel (d)]')
            print('[Inventory (i)]')
            destination = input('>>>')
            if destination == 'a':
                os.system('clear')
                World.Tavern()
            elif destination == 'b':
                os.system('clear')
                World.Harbor()
            elif destination == 'c':
                os.system('clear')
                World.Market()
            elif destination == 'd':
                os.system('clear')
                World.Brothel()
            elif destination == 'i':
                os.system('clear')
                stats()
            else:
                City()

    
    def Tavern():
        character.loc.clear()
        character.loc.update({'Tavern' : 1})
        if glu.keys in character.keys:
            print('You enter a whimsical and cheerful tavern. The place is full of happy an merry drunks and bums.')
            print('Everything seems to be incredibly fun. The owner is behind the bar, ready to serve drinks to anyone.')
            print('What do you do?')
            print('[Get a beer (a)]       [Leave (b)]')
            choice = input('>>>>')
            if choice == 'a':
                merchants.TavernOwner()
                pass
            else:
                os.system('clear')
                World.City()
        else:
            print('You enter a whimsical and cheerful tavern. The place is full of happy an merry drunks and bums.')
            print('Everything seems to be incredibly fun. The owner is behind the bar, ready to serve drinks to anyone.')
            print('At a distant table though an orc is giving you the stink eye.')
            print('What do you do?')
            print('[Get a beer (a)]       [Leave (b)]      [Approach the orc (c)]')
            choice = input('>>>>')
            if choice == 'a':
                merchants.TavernOwner()
                pass
            elif choice == 'b':
                os.system('clear')
                World.City()
            elif choice == 'c':
                os.system('clear')
                World.TavernOrc()
            else:
                pass

    def Harbor():
        character.loc.clear()
        character.loc.update({'Harbor' : 2})
        if thief.keys in character.keys:
            print("Let's try not to push your luck and just go somewhere safer, shall we?")
            print('What do you do?')
            print('[Leave (b)]')
            choice = input('>>>>')
            if choice == 'a':
                os.system('clear')
                World.City()
            else:
                os.system('clear')
                World.City()
        else:
            print('You are at the harbor. Ships from all over the 12 seas come and go here. Fresh fishy breeze fills your lungs and caresses your face.'
                  '\nsailors and pirates walk around in a busy mess of humans that shout at each other and interact in the least fashionable ways.'
                  '\n It seems like a great place to have a walk!')
            print('[Have a walk (a)]       [Leave (b)]')
            choice = input('>>>>')
            if choice == 'a':
                os.system('clear')
                World.HarborThief()

            else:
                os.system('clear')
                World.City()

    def Brothel():
        character.loc.clear()
        character.loc.update({'Brothel' : 4})
        os.system('clear')
        if mongl.keys not in character.keys:
            print('You enter a barely lit brothel that looks everything but the cool one in GoT.')
            print('Obviously, there are many different women from many different continents who do not wear very different clothes')
            print('since they are all naked. The smell of passion, love and STD fills every corner of the crumbling building.')
            print('What do you do?')
            print('[Talk to one of the girls (a)]       [Leave (b)]')
            choice = input('>>>>')
            if choice == 'a':
                World.BrothelGoblin()
                pass
            else:
                os.system('clear')
                World.City()
        else:
            print("You probably had enough of the brothel for today, don't you think?")
            print('[ (a)]       [Leave (b)]')
            choice = input('>>>>')
            if choice == 'a':
                merchants.TavernOwner()
                pass
            elif choice == 'b':
                os.system('clear')
                World.City()
            elif choice == 'c':
                os.system('clear')
                TavernOrc()
            else:
                pass

    def BrothelGoblin():
        os.system('clear')
        print('You approach the only half clothed lady in the brothel, her long dark hair remind you vaguely your cousin.\n'
              'She is giving you her back (no pun intended) and you gently lay your hand on her shoulder.\n'
              'As soon as she turns her long hair drop on the floor, revealing it was a wig and that she is not a woman!')
        time.sleep(8)
        os.system('clear')
        print(asciart.GoblinArt)
        print('"Come one! Give us a kiss!"\n')

        print('The Goblin just challenged you. What do you do?')
        print('[Slap him with your silk glove and accept (a)]       [Leave the place along with your pride and balls (b)]')
        choice = input('>>>>')
        if choice == 'a':
            print(' ')
            init(mongl)
        else:
            World.Brothel()

    def TavernOrc():
        os.system('clear')
        print(asciart.OrcArt)
        print('What are you looking at puny creature? Are you looking for a fight?')
        print(' ')
        print('The orc just challenged you. What do you do?')
        print(
            '[Slap him with your silk glove and accept (a)]       [Leave the place along with your pride and balls (b)]')
        choice = input('>>>>')
        if choice == 'a':
            print(' ')
            init(glu)
        else:
            os.system('clear')
            World.Tavern()

    def HarborThief():

        print('You are walking along the seaside, where many men are fighting, shouting and loading cargos up on the ships.'
              '\nA nice dark alley seems the perfect place to end you relaxing walk.'
              '\nObviously, a thief comes out with a huge knife in his hand ready to gut you')
        time.sleep(7)
        os.system('clear')
        print(asciart.ThiefArt)
        print('"The bag or the life lady!"\n')

        print('The thief just challenged you. What do you do?')
        print('[Slap him with your silk glove and accept (a)]       [Leave the place along with your pride and balls (b)]')
        choice = input('>>>>')
        if choice == 'a':
            print(' ')
            init(thief)
        else:
            os.system('clear')
            World.Harbor()

    def Market():
        merchants.MarketMerchant()
        pass

    def Boss():
        os.system('clear')
        print('Dear lord, here we go again... Those peasants are for the billionth time being attacked by a dragon.\n'
              'Guess a vacation is out of question right now... Such a shame since they are having sales at the brothel.\n'
              'Anyway, now you are facing the dragon! He spits fire, flies, all of that shit.\n'
              'Fight him and save those commoners!')
        time.sleep(9)
        os.system('clear')
        print(asciart.boss)
        time.sleep(4)
        os.system('clear')
        init(boss)
