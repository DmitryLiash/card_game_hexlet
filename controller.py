import view
"""
1. Приветствие
2. Выбор уровня
3. Игра
4. Выход/Продолжение игры

"""


def start():
    flag = True
    while flag:
        random_card = view.random_card()
        print(f"\n----------------\nОтвет для тестирования: {random_card}\n--------------")  # спойлер убрать
        user_lvl_select = view.hello_lvl_selection()
        if user_lvl_select == 1:
            view.game_lvl1(random_card)
        elif user_lvl_select == 2:
            view.game_lvl2(random_card)
        elif user_lvl_select == 3:
            view.game_lvl3(random_card)
        else:
            flag = False
