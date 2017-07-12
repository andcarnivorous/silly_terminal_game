class Character:

    def __init__(self, name, lp, attk, arm, mana, money, keys, loc):
#        self.place = name
        self.name = name
        self.lp = lp
        self.attk = attk
        self.arm = arm
        self.mana = mana
        self.money = money
        self.keys = keys
        self.loc = loc
    

class Inventory:
    def __init__(self, itemarm, itemdmg, itemmana, jwlname, armname, wpnname, jwlinfo, arminfo, wpninfo):
        self.itemarm = itemarm
        self.itemdmg = itemdmg
        self.itemmana = itemmana
        self.jwlname = jwlname
        self.armname = armname
        self.wpnname = wpnname
        self.jwlinfo = jwlinfo
        self.arminfo = arminfo
        self.wpninfo = wpninfo
        
        
        
        
character = Character(input('What is your name?\n'), 20, 2, 0, 0, 0, [], {})

charinv = Inventory(0,0,0,[],[],[],[],[],[])

print('Greetings fellow wanderer! I heard they call you', character.name, "\n But I'm not going to bother too much with that.")
print('\n Before adventuring in your long kick-ass journey, tell me... \n Which race do you choose?')
print('Choose Human (h), Elf (e), Dwarf (d)')
chrace = input(">>>")
