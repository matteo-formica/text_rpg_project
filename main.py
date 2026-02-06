import random
import math


class Action:
    def __init__(self, name, type, level=1, range=()):
        self.name = name
        self.type = type
        self.level = level
        self.range = range

class Magic:
    def __init__(self, name, type, level=1, effect=1, range=()):
        self.name = name
        self.type = type
        self.level = level
        self.effect = effect
        self.range = range


class Skill:
    def __init__(self, name, type, level=1, effect=1, range=()):
        self.name = name
        self.type = type
        self.level = level
        self.effect = effect
        self.range = range


class Object:
    def __init__(self, name, type, level=1, effect=1):
        self.name = name
        self.type = type
        self.level = level
        self.effect = effect


class Weapon:
    def __init__(self, name, type, level=1, damage=1, rarity="Common"):
        self.name = name
        self.type = type
        self.level = level
        self.damage = damage
        self.rarity = rarity


class Armor:
    def __init__(self, name, level=1, shield= 1):
        self.name = name
        self.level = level
        self.shield = shield


class Enemy:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.armor = round((self.level*1.3), 1)
        self.damage = round((self.level*1.5), 1)
        self.full_life = (self.level*4)
        self.life = (self.level*4)
        self.exp = self.level*2

class Character:
    def __init__(self, name, armor, weapon, level=1, full_life =10, life=10, skills={}, magic={}, actions={}, inventory ={}):
        self.name = name
        self.level = level
        self.full_life = full_life
        self.life = life
        self.armor = armor
        self.weapon = weapon
        self.skills = skills
        self.magic = magic
        self.actions = actions
        self.inventory = inventory
        self.exp = 0
        self.exp_thresh = 5

    def act(self, action_required, action_level_required, roll_required):
        while True:
            print("Actions available:")
            print("---------------------------")
            for key in self.actions.keys():
                print(f"{key}", sep="|")
            print("---------------------------")
            action = self.actions[input("Choose an action to perform: ").title()]
            if action.name == action_required and action.level == action_level_required:
                print(f"{roll_required} required to complete this action")
                try_roll = input("Press any key to try..")
                roll = random.randint(min(action.range), max(action.range))
                print()
                print("----------------------------------------------")
                print(f"You rolled: {roll}")
                if roll >= roll_required:
                    print()
                    print("----------------------------------------------")
                    print("Action completed")
                    print("----------------------------------------------")
                    return True
                else:
                    print()
                    print("----------------------------------------------")
                    print("Action failed")
                    print("----------------------------------------------")
                    return False
            else:
                print()
                print("Wrong Action! Choose the right one..")

    def attack(self, enemy):
        damage_value = (self.level * self.weapon.damage) - (enemy.level * enemy.armor)
        if damage_value < 0:
            damage_value = 0
        enemy.life -= damage_value
        print()
        print()
        print("----------------------------------------------")
        print(f"You dealt {damage_value} damage with your {self.weapon.name}, enemy has {enemy.life} life points remaining")
        print("----------------------------------------------")
        return enemy.life
    
    def defense(self, enemy):
        damage_value = (enemy.level * enemy.damage) - (self.level * self.armor.shield)
        if damage_value < 0:
            damage_value = 0
        self.life -= damage_value
        print()
        print()
        print("----------------------------------------------")
        print(f"Enemy dealt {damage_value} damage, you have {self.life} life points remaining")
        print("----------------------------------------------")
        return self.life

    def skill_attack(self, enemy):
        print("Skills available:")
        print("---------------------------")
        for key in self.skills.keys():
            print(f"{key}", sep="|")
        print("---------------------------")
        skill_name = input("Choose a skill: ").title()
        skill = self.skills[skill_name]
        damage_value = (skill.effect * self.level) - (enemy.level * enemy.armor)
        if damage_value < 0:
            damage_value = 0
        enemy.life -= damage_value
        print()
        print()
        print("----------------------------------------------")
        print(f"You dealt {damage_value} damage, enemy has {enemy.life} life points remaining")
        print("----------------------------------------------")
        return enemy.life
    
    def magic_attack(self, enemy):
        print("Magic available:")
        print("---------------------------")
        print(f"{self.magic.keys}", sep="|")
        print("---------------------------")
        magic_name = input("Choose a magic: ").title()
        magic = self.magic[magic_name]
        damage_value = (magic.effect * self.level) - (enemy.level * enemy.armor)
        if damage_value < 0:
            damage_value = 0
        enemy.life -= damage_value
        print()
        print()
        print("----------------------------------------------")
        print(f"You dealt {damage_value} damage, enemy has {enemy.life} life points remaining")
        print("----------------------------------------------")
        return enemy.life
    
    def use_object(self, enemy):
        print("Bag:")
        print("---------------------------")
        for key in self.inventory.keys():
            print(f"{key}", sep="|")
        print("---------------------------")
        object_name = (input("Choose an object to use: ")).title()
        if (self.inventory[object_name]).type == "heal":
            self.life += (self.inventory[object_name]).effect
            if self.life > self.full_life:
                self.life = self.full_life
            self.inventory.pop(object_name)
            print()
            print()
            print("----------------------------------------------")
            print(f"You now have {self.life} life points")
            print("----------------------------------------------")
        else:
            enemy.life -= (self.inventory[object_name]).effect
            print(f"You thrown {(self.inventory[object_name].name)} and you dealt {(self.inventory[object_name]).effect} damage points")
            print(f"Enemy's life: {enemy.life}")
    def level_up(self, rem=0):
        print()
        print()
        print("----------------------------------------------")
        print("LEVEL UP!")
        self.level += 1
        self.life = self.full_life
        print(f"You reached level {self.level}")
        self.exp = 0
        self.exp_thresh += round((self.exp_thresh/100 * 10), 1)
        self.full_life += self.level
        self.life += self.level
        print(f"Stats up..")
        print(f"Life points: {self.life} | Next level by {self.exp_thresh} points")
        print("----------------------------------------------")
        if rem:
            self.exp_gain(self, rem)

    def exp_gain(self, enemy, rem=0):
        if rem:
            print()
            print()
            print("----------------------------------------------")
            print(f"You gained {rem} exp points")
            print("----------------------------------------------")
            self.exp += rem
            if self.exp == self.exp_thresh:
                self.level_up(self)
            elif self.exp > self.exp_thresh:
                rem = self.exp - self.exp_thresh
                self.level_up(rem)

            else:
                print()
                print(f"Remaining points to level up: {self.exp_thresh - self.exp}")
                print("----------------------------------------------")
        else:
            print()
            print()
            print("----------------------------------------------")
            print(f"You gained {enemy.exp} exp points")
            print("----------------------------------------------")
            self.exp += enemy.exp

            if self.exp == self.exp_thresh:
                self.level_up(self)
            elif self.exp > self.exp_thresh:
                rem = self.exp - self.exp_thresh
                self.level_up(rem)

            else:
                print()
                print()
                print(f"Remaining points to level up: {self.exp_thresh - self.exp}")
                print("----------------------------------------------")
