import os
import time
import random

# File code
from classFigure import Hero
from hero import all_Heroes

# Define functions
# Utilities functions
def closed():
    time.sleep(1)
    os.system('cls')


# Hero functions
def printHero(Heroes):
    for index, hero in enumerate(Heroes):
        print(f"({index+1}). {hero.getName}")


def makeHero(Heroes):
    name = input("Nama : ")
    hp = int(input("HP : "))
    atk = int(input("Atk : "))
    defs = int(input("Def : "))
    arm = int(input("Armor : "))
    level = int(input("Level : "))
    eva = int(input("Evasion : "))
    new_hero = Hero(name, hp, atk, defs, arm, level, eva)
    Heroes.append(new_hero)


def detailsHero(index, sides):
    print("\n", "=" * 20)
    print(f"\nAnda Memilih {all_Heroes[index].getName} sebagai {sides}")
    print(f"Berikut adalah Detail {sides} yang Anda pilih : ")
    print(f"\n{all_Heroes[index].getInfo}")
    print("\n", "=" * 20)


# choosen functions
def choose_hero(all_Heroes):
    while True:
        # if state not in locals():
        s1 = input("\nMau Pilih (P) Hero yang sudah ada atau Buat (B) sendiri? (P/B) : ").strip().upper()

        if s1 == "B":
            print("\nBuat Hero Anda!")
            makeHero(all_Heroes)
            return len(all_Heroes) - 1
        
        elif s1 == "P":
            num = int(input("\nPilih Hero untuk Duel! : "))
            temp = num

            # state = s1
            if temp > len(all_Heroes):
                print("Pilih yang ada di list kontol!")
                state = s1
                continue
                
            return num - 1

        else:
            print("Ketik P/B bodoh!")


def choose_enemy(all_Heroes, hero_index):
    printHero(all_Heroes)
    while True:
        enemy_index = int(input("\nPilih Lawan untuk Duel! : ")) - 1
        if 0 <= enemy_index < len(all_Heroes) and enemy_index != hero_index:
            return enemy_index
        print("Pilih lawan yang ada di list dan jangan pilih hero yang sama!")


# Action functions
def enemyAction(Hero, Enemy, all_Heroes):
    # var def
    enemy_name = all_Heroes[Enemy].getName
    hero_name = all_Heroes[Hero].getName
    actionE = random.randint(1, 4)
    attempsList = []

    # for attack
    if actionE == 1:
        hp_hero = all_Heroes[Enemy].attack(all_Heroes[Hero])
        if hp_hero == 0:
            print(f"{enemy_name} : Kamu {hero_name} telah mati..")
            return 0


    # for defend
    elif actionE == 2:
        pass


    # for skill
    elif actionE == 3:
        pass


    # for escape
    elif actionE == 4:
        zeroIs, attemp = all_Heroes[Enemy].escape(all_Heroes[Hero], attempsList)
        if zeroIs == 0:
            print(f"{enemy_name} : Berhasil kabur dari {hero_name}")
            return 0

        print(f"{enemy_name} : Gagal kabur dari {hero_name}")
        attempsList.append(attemp)



def gameAction(Hero, Target, all_Heroes):
    # var def
    target_name = all_Heroes[Target].getName
    hero_name = all_Heroes[Hero].getName
    actionList = ["Attack", "Defends", "Skill", "Escape"]
    attempsList = []

    # run the action event
    while True:

        for i, action in enumerate(actionList):
            print(f"({i+1}). {action}")

        action = int(input("\nPilih Aksimu beb : "))
        print("")
        
        # for attack
        if action == 1:
            hp_target = all_Heroes[Hero].attack(all_Heroes[Target])
            if hp_target == 0:
                print(f"{hero_name} : Lawanmu {target_name} telah mati..")
                print("KAMU MENANG")
                break

            # enemy takes action
            enemyACT = enemyAction(Hero, Target, all_Heroes)
            if enemyACT == 0:
                print("\nEND UNTUK BOCAH TOLOL KEK KAMU (KALAH)")
                break


        # for defend
        elif action == 2:
            # enemy takes action
            enemyAction(Hero, Target, all_Heroes)
            pass

    
        # for skill
        elif action == 3:
            # enemy takes action
            enemyAction(Hero, Target, all_Heroes)
            pass

        
        # for escape
        elif action == 4:
            zeroIs, attemp = all_Heroes[Hero].escape(all_Heroes[Target], attempsList)
            if zeroIs == 0:
                print(f"{hero_name} : Berhasil kabur dari {target_name}")
                break

            print(f"{hero_name} : Gagal kabur dari {target_name}")
            attempsList.append(attemp)

            # enemy takes action
            enemyEva = enemyAction(Hero, Target, all_Heroes)
            if enemyEva == 0:
                print("KAMU KALAH")
                break



        # break state
        breakOr = input("\nAksi lagi? y/n : ").lower()
        if breakOr == 'n' or breakOr == 'nigga':
            break
