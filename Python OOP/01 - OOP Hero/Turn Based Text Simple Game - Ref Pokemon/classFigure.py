import os
import time
import random

# This section for class declare
# Define class
class Hero:
    count = 0

    # Initial of main stats
    def __init__(self, name, hp, atk, defs, arm, lvl, evasion):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__defs = defs
        self.__arm = arm
        self.__lvl = lvl # max lvl = 1000
        self.__eva = evasion # max 100 percent
        Hero.count += 1
        self.i = Hero.count

    # Atribut get Info
    @property
    def getInfo(self):
        return f"\nName : {self.__name}\nHealth : {self.__hp}\nAttack : {self.__atk}\nDefense : {self.__defs}\nArmor : {self.__arm}\nLevel : {self.__lvl}\nEvasion : {self.__eva}"

    # Atribut get Name
    @property
    def getName(self):
        return f"{self.__name}"

    # Piece of shit, i mean sub_func
    def attack(self, target):
        tempHP = target.__hp
        targetStat = target.__hp
        damage = self.__atk + (self.__lvl * 10)

        result = targetStat - damage
        target.__hp = result

        # if target died
        if target.__hp <= 0:
            target.__hp = 0
            print(f"{self.__name} : The Damage is {damage}. HP {target.__name} from {tempHP} to {target.__hp}. The enemy died")
            return target.__hp

        print(f"{self.__name} : The Damage is {damage}. HP {target.__name} from {tempHP} to {target.__hp}")
        return target.__hp
    
    def defend(self):
        pass


    def skill(self):
        pass


    def escape(self, target, attemps):
        attempsTotal = len(attemps)
        chanceList = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
        chance = (100 // self.__eva) + 1
        probability = random.randint(self.__eva, 100)

        if probability in chanceList:
            return 0, probability
        if attempsTotal == chance:
            return 0, probability
        
        return 1, probability