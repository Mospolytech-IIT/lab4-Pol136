"""
Модуль для запуска функций лабораторной
"""

from all_tasks import (feed_cat, play_with_cat, train_cat, groom_cat, show_cat,
                       squeeze_cat, give_medicine, count_cats)


def do_all_with_pet():
    """
    Запускает все функции
    """
    try:
        feed_cat("Пушок", "мясо")
        feed_cat("Пушок", "каша")
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()

    try:
        play_with_cat("Дурачок", "мышка")
        play_with_cat("Дурачок", 123)
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    train_cat("Персик", "дать лапу")
    print()
    train_cat("Персик", "кувырок")
    print()

    groom_cat("Пес", "щетка")
    print()
    groom_cat("Пес", "перчатки")
    print()

    show_cat("Калькулятор", "Полина")
    print()
    show_cat("Калькулятор", 123)
    print()
    show_cat("Калькулятор", "Олег")
    print()

    squeeze_cat("Морковка", True)
    print()
    squeeze_cat("Морковка", "пнуть")
    print()
    squeeze_cat("Морковка", "жамкнуть")
    print()

    give_medicine("Пушочек", "валерьянка")
    print()
    give_medicine("Пушочек", "парацетомол")
    print()

    count_cats(3, 10)
    count_cats(11, 10)
    count_cats(0, 9)
    count_cats("five", 6)


if __name__ == '__main__':
    do_all_with_pet()
