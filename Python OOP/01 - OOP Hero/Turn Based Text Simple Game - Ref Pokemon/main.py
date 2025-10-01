import os
import time
import random

# File code
from functionEtc import *
closed()

# Run the game shit
while True:
    closed()
    # Intro the Game sucks
    print("\nWELCOME TO THE TURN BASED TEXT SIMPLE GAME")

    runIs = input("\nReady? : ").lower()
    if runIs == 'n':
        break
    elif runIs != 'y':
        print("Get serious bro, type 'Y'")
        continue

    # Let the game begins
    printHero(all_Heroes)
    hero_index = choose_hero(all_Heroes)
    enemy_index = choose_enemy(all_Heroes, hero_index)
    closed()

    # Print hero and enemy
    detailsHero(hero_index, "Hero")
    detailsHero(enemy_index, "Enemy")

    # Main Event
    gameAction(hero_index, enemy_index, all_Heroes)


    # Break STATE or Other Games
    otherGames = input("\nOther Games? y/n : ").lower()
    if otherGames in ['n', 'nigga']:
        break
    closed()




