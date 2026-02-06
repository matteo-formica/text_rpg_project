from main import Character
from actions import actions
from skills import skills
from armor import armor
from weapon import weapon
from objects import objects
import random as r
import combat
from stages import stages

class Story:
    def __init__(self, first_character, stages):
        self.protagonist = first_character

    def stage_control(self, first_character, path):
        print()
        print("----------------------------------------------")
        print(stages[path].intro)
        print("----------------------------------------------")
        print()
        path = int((input("Where you want to go?(option number): ")).strip())
        self.stage_control(first_character, stages[path])




def init_adventure():
    print("Welcome to my text-based RPG Adventure")
    print("----------------------------------------------")
    print()
    name = (input("Choose your name: ")).title()
    goon = input(f"{name} Press any key to drop an armor and a weapon to start your adventure..")
    armr = armor[r.randint(0, (len(armor) - 1))]
    wpn = weapon[0][r.randint(0, (len(weapon[0]) - 1))]
    skill_1 = skills[r.randint(0 , (len(skills) - 1))]
    skill_2 = skills[r.randint(0 , (len(skills) - 1))]
    act_1 = actions[1]
    skll = {skill_1.name : skill_1, skill_2.name : skill_2}
    acts = {act_1.name : act_1}
    first_character = Character(name, armr, wpn, skills=skll, actions=acts)
    print("----------------------------------------------")
    print(f"Okay {first_character.name} you'll start at level {first_character.level}")
    print(f"You take your {wpn.name} and you wear {armr.name}")
    print(f"You learnt to {acts[act_1.name].name}")
    print(f"You learnt {len(skll)} skills:")
    for skill in skll:
        print(f"- {skll[skill].name}")
    print("----------------------------------------------")
    print()
    goon = input("Press any key to start your journey")
    return first_character

def encounter(first_character, stage_level=1):
    enemy = combat.spawn(stage_level)
    print()
    print()
    print("----------------------------------------------")
    print(f"You encountered a {enemy.name}")
    print("----------------------------------------------")
    fight = combat.turn(first_character, enemy)
    if fight:
        print()
        print()
        print("----------------------------------------------")
        print("You found a chest..")
        print("----------------------------------------------")
        act = first_character.act("Open", 1, 5)
        if act:
            rarity = r.randint((stage_level - 1), (len(weapon) - 1))
            rarity2 = r.randint((stage_level - 1), (len(objects) - 1))
            reward = weapon[rarity][r.randint(0, (len(weapon[rarity]) - 1))]
            reward2 = objects[rarity2][r.randint(0, (len(objects[rarity2]) - 1))]
            disposable_inventory = {reward.name : reward}
            print()
            print("----------------------------------------------")
            print(f"You dropped  a {disposable_inventory[reward.name].rarity} {disposable_inventory[reward.name].name} | level:{disposable_inventory[reward.name].level} | damage:{disposable_inventory[reward.name].damage}")
            print("----------------------------------------------")
            change = (input(f"Do you want to change your {first_character.weapon.name} | Level: {first_character.weapon.level} | Damage: {first_character.weapon.damage} with {disposable_inventory[reward.name].name}?(y/n): ")).lower()
            if change == "n":
                pass
            else:
                first_character.weapon = disposable_inventory[reward.name]
            print("----------------------------------------------")
            print(f"You dropped a {reward2.name} | Type: {reward2.type} | Level: {reward2.level} | Effect: {reward2.effect}")
            print(f"{reward2.name} added to inventory")
            print("----------------------------------------------")
            first_character.inventory[reward2.name] = reward2
        else:
            pass


first_character = init_adventure()
while True:
    encounter(first_character)


