from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1
    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

def training(training_type):
    for i in range(0, 100, 20):
        print(f"тренировка завершена на {i}%")
        sleep(1.5)
    if training_type == '1':
        if player["money"] >= 1000:
            player["attack"] +=2
            player["money"] -=1000
            print(f"тренировка окончена. Ваша величина атаки {player['attack']}")
        else:
            print(f"ошибка, недостаточно средст. Баланс:{player['money']}")

    if training_type == "2":
        if player["money"] >= 800:
            player["armor"] -=0.05
            player["money"] -=800
            print(f"тренировка окончена. Ваша защита равна {100 - player['armor'] * 100}")
        else:
            print(f"ошибка, недостаточно средст. Баланс:{player['money']}")

def display_player():
    print(f"Игрок - {player['name']}")
    print(f"Атака - {player['attack']}")
    print(f"Броня - {player['armor']}")
    print(f"ХП - {player['hp']}")

def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f"Враг - {enemy['name']}")
    print(f"Атака - {enemy['attack']}")
    print(f"ХП - {enemy['hp']}")
def inventory():
    print("у вас есть:")
    for value in player['inventory']:
        print(value)
    print(f"{player['money']} монет")
    print()
    kl = input("что желаешь активировать?")
    if kl == '+крит. урон':
        if '+крит. урон' in player['inventory']:
            potion = input("""активировать?
            1-да
            2-нет
            """)
            if potion =='1':
                player['luck'] += 10
                print(f"ваш шанс крит. урона рвен {player['luck']}%")
                player['inventory'].remove('+крит. урон')
    elif kl == 'пропуск силовой тренировки':
        if 'пропуск силовой тренировки' in player['inventory']:
            potion = input("""активировать?
            1-да
            2-нет
            """)
            if potion =='1':
                player["attack"] +=2
                print(f"ваш урона рвен {player['attack']}")
                player['inventory'].remove('пропуск силовой тренировки')
    elif kl == 'пропуск тренировки по самообороне':
        if 'пропуск тренировки по самообороне' in player['inventory']:
            potion = input("""активировать?
            1-да
            2-нет
            """)
            if potion =='1':
                player["armor"] -=0.05
                print(f"Ваша защита равна {100 - player['armor'] * 100}")
                player['inventory'].remove('пропуск тренировки по самообороне')
    elif kl == 'аптечка':
        if 'аптечка' in player['inventory']:
            potion = input("""активировать?
            1-да
            2-нет
            """)
            if potion =='1':
                player["hp"] +=20
                print(f"Ваше здоровье равнщ {player['hp']}")
                player['inventory'].remove('аптечка')
def shop():
    print("привет!")
    print(f"баланс:{player['money']}")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")
    
    item = input("что нужно:")
    if item in player['inventory']:
        print(f"у тебя максимальное количество предметов {player[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]['price']
    else:
        print("недостаточно средств")
def earn():
    print("добро пожаловать в гилдию. Вы можете поучаствовать в лотереи")
    result = randint(1,100)
    sleep(1.5)
    print("все получили билеты?")
    if result <= 5:
        print("вы выйграли 5000 монет")
        player['money'] += 5000
    elif result <= 20:
        print("вы выйграли 2000 монет")
        player['money'] += 2000
    elif result <= 50:
        print("вы выйграли 1000 монет")
        player['money'] += 1000
    elif result <= 100:
        print("вы выйграли 500 монет")
        player['money'] += 500
    print(f"баланс:{player['money']}")