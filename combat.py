from main import Character
from enemy import enemies
import random

def turn(protagonist, enemy):
    while True:
        print()
        print()
        print("----------------------------------------------")
        print(f"{protagonist.name}'s turn:")
        print("1. Attack | 2. Skill | 3. Magic | 4. Bag | 5. Pass")
        print()
        print("----------------------------------------------")
        select = int(input("Choose an action to perform: "))
        match select:
            case 1:
                protagonist.attack(enemy)
            case 2:
                protagonist.skill_attack(enemy)
            case 3:
                protagonist.magic_attack(enemy)
            case 4:
                protagonist.use_object(enemy)
            case 5:
                pass
        
        if enemy.life <= 0:
            print("----------------------------------------------")
            print("You won")
            print("----------------------------------------------")
            enemy.life = enemy.full_life
            protagonist.exp_gain(enemy)
            return True
        else:
            print()
            print()
            print("----------------------------------------------")
            print("Enemy's turn:")
            print()
            protagonist.defense(enemy)
            if protagonist.life <= 0:
                print("----------------------------------------------")
                print("You loose..")
                print("----------------------------------------------")
                return False


def spawn(level):
    if level > len(enemies):
        level = 0
    enemy = enemies[level - 1][random.randint(0, (len(enemies[level -1]) - 1))]
    
    return enemy




