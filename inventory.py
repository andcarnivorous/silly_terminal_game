
class Item:
    def __init__(self, name, info, dmg, arm, mana):
        self.name = name
        self.info = info
        self.dmg = dmg
        self.arm = arm
        self.mana = mana


class Weapon(Item):
    pass

badile = Weapon("Shovel", "", 3,0,0)

padella = Weapon("Pan", "", 1,0,0)

spada = Weapon("Sword", "", 2,0,0)

bazooka = Weapon("Bazooka", "", 5,0,0)

class Armor(Item):
    pass

tutu = Armor("Tutù", "",0,1,0)

sospensorio = Armor("Jockstrap", "", 0,2,0)

space_suit = Armor("Space Suit", "", 0,5,0)

class Jewel(Item):
    pass

ring = Jewel("Ring", "", 0,0,1)

necklace = Jewel("Necklace", "", 0,0,2)

cockring = Jewel("Cockring","", 0,0,3)

items = [badile, padella, spada, bazooka, tutu, sospensorio, space_suit]
