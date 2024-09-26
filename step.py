from random import randint
from time import sleep
from data import *
from heplers import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = randint(0, 2)

while True:
    action = input("""Выберите действие:
1-бой
2-тренировка
3-информация об игроке
4-информация о текущем противнике
5-магазин
6-получить валюту
7-показать и нвертарь 
""")
    if action == "1":
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == "2":
        training_type = input("""
1-тренировать атаку
2-тренировать оборону
""")
        training(training_type)
    elif action == "3":
        display_player()
        print()
    elif action == "4":
        display_enemy(current_enemy)
        print()
    elif action == "5":
        shop()
    elif action == "7":
        inventory()
    elif action == "6":
        earn()