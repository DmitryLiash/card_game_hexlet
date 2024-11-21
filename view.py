import random
from random import choice
import txt
import time


def random_card() -> str:
    return f"{choice(txt.card_suits)} {choice(txt.card_values)}"


def check_lvl_selection() -> int:
    while True:
        enter_from_user = input(txt.lvl_annotation)
        if enter_from_user.isdigit() and enter_from_user in ["1", "2", "3", "4"]:
            return int(enter_from_user)
        else:
            print("Ошибка ввода. Попробуйте еще раз")
            time.sleep(1)


def hello_lvl_selection() -> int:
    print(txt.lvl_select_txt)
    value = check_lvl_selection()
    return value


def game_lvl1(card: str):
    color = ['red', 'black']
    flag = True
    while flag:
        while True:
            answer = input("Введите цвет масти- 'red' или 'black': ").lower()
            if answer in color:
                if answer == color[0] and card[0] in ["♥", "♦"] or answer == color[1] and card[0] in ["♣", "♠"]:
                    print(f"{random.choice(txt.win_list)}\nКарта была: {card}")
                    time.sleep(4)
                    print("\n" * 100)   # заменить на system('cls') при сборки
                    break
                else:
                    print("Не правильно. Попробуйте еще раз")
                    time.sleep(1)
            else:
                print("Ошибка ввода. Попробуйте еще раз")
                time.sleep(1)
        flag = False


def game_lvl2(card: str):
    count = 0
    flag = True
    while flag:
        while True:
            answer = input("Введите ранг карты(2, 3, ..., 10. 'jack', 'queen', 'king', 'ace': ").lower()
            if answer in txt.card_values:
                if answer == card[2:]:
                    print(f"\n{random.choice(txt.win_list)}\nКарта была: {card}\nВам понадобилось попыток: {count}")
                    time.sleep(4)
                    print("\n" * 100)  # заменить на system('cls') при сборки
                    break
                else:
                    print("Не правильно. Попробуйте еще раз")
                    count += 1
                    time.sleep(1)
            else:
                print("Ошибка ввода. Попробуйте еще раз")
                time.sleep(1)
        flag = False


def select_suits() -> str:
    while True:
        enter_from_user = input(txt.sell_suits_annotation)
        if enter_from_user.isdigit() and enter_from_user in ["1", "2", "3", "4"]:
            return txt.dict_sell_suits_annotation.get(enter_from_user)
        else:
            print("Ошибка ввода. Попробуйте еще раз")
            time.sleep(1)


def game_lvl3(card: str):
    count = 0
    flag = True
    while True:
        suits_user = select_suits()
        answer = input("Введите ранг карты(2, 3, ..., 10. 'jack', 'queen', 'king', 'ace': ").lower()
        if answer in txt.card_values:
            if suits_user + " " + answer == card:
                print(f"\n{random.choice(txt.win_list)}\nКарта была: {card}\nВам понадобилось попыток: {count}")
                time.sleep(4)
                print("\n" * 100)  # заменить на system('cls') при сборки
                break
            else:
                print("Не правильно. Попробуйте еще раз")
                count += 1
                time.sleep(1)
        else:
            print("Ошибка ввода. Попробуйте еще раз")
            time.sleep(1)
    flag = False
