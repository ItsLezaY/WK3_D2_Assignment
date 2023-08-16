# Exercise 1 Option 2

# Create A Video Game Character Class using Object-Oriented Programming

# The character class should have the following attributes: character type (i.e. ogre, human, elf, etc), health points, attack points, weapons (list or dictionary). The class should also have the following methods to deplete health points, regain health points, add or remove weapons, and show character stats.

class Character():

    RACE = 'High Elf'

    def __init__(self, name, class_type, hp, ap, weapons):
        self.name = name
        self.class_type = class_type
        self.hp = hp
        self.ap = ap
        self.weapons = []

    def char_stats(self):
        print(f"\n\t{self.name} \n\n\t{self.RACE}\n\t{self.class_type}\n\n\tHP: {self.hp}\n\tAP: {self.ap}\n\tWeapon: {self.weapons}")

    def damage_taken(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal_hp(self, healing):
        self.hp += healing

    def equip_weapon(self, weapon):
        self.weapons.append(weapon)

    def unequip_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
        elif weapon not in self.weapons:
            print("That weapon is not in your arsenal.")

thea = Character('Thea', 'Archer', 1200, 100, weapons='')

thea.char_stats()

damage = int(input("\nEnter damage taken: "))
thea.damage_taken(damage)
print("You have taken damage: ")
thea.char_stats()

healing = int(input("\nEnter healing amount: "))
thea.heal_hp(healing)
print("You have recovered HP: ")
thea.char_stats()

new_weapon = input("\nEnter weapon to add: ")
thea.equip_weapon(new_weapon)
print("Equipped weapon: ")
thea.char_stats()

remove_weapon = input("\nEnter weapon to remove: ")
thea.unequip_weapon(remove_weapon)
print("Unequipped weapon: ")
thea.char_stats()





#Exercise 2 

# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

class stringMethods():

    def get_string(self):
        self.user_input = input("Enter a string: ")

    def print_string(self):
        print(self.player_string.upper())

stringMethods = stringMethods()

stringMethods.get_string()
stringMethods.print_string()

