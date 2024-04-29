import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword, fists
from weapon import Weapon


def choose_weapon() -> Weapon:
    print("Choose your weapon:")
    print("1. Iron Sword")
    print("2. Short Bow")
    print("3. Fists")
    while True:
        choice = input("Enter the number of the weapon you want to use: ")
        if choice == "1":
            return iron_sword
        elif choice == "2":
            return short_bow
        elif choice == "3":
            return fists
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


hero_weapon = choose_weapon()
hero = Hero(name="Hero", health=100)
hero.equip(hero_weapon)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
