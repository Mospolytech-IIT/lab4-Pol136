"""
Модуль с реализацией заданий 1-5 из лабораторной
"""

import random


# 1 задание
def feed_cat(cat_name, food_type):
    """
      Кормит кота
      """
    if food_type not in ["рыба", "мясо", "птица"]:
        raise ValueError(f"Кот {cat_name} не ест {food_type}!")

    print(f"Кот {cat_name} ест {food_type}")


def play_with_cat(cat_name, toy):
    """
    Играет с котом
    """
    if not isinstance(toy, str):
        raise TypeError(f"Нельзя играть с {toy}! Это не игрушка")

    print(f"Кот {cat_name} играет с {toy}")


# 2 задание
def train_cat(cat_name, trick):
    """
    Обучает кота трюку
    """
    if not isinstance(trick, str):
        raise ValueError(f"Не получится обучить кота {cat_name} трюку {trick}!")

    print(f"Кот {cat_name} пытается выучить трюк: {trick}...")
    try:
        if trick == "кувырок":
            raise ValueError("Кот не понял команду!")
        print(f"Кот {cat_name} выучил трюк: {trick}!")
    except Exception as e:
        print(f"Ошибка! {e}")


# 3 задание
def groom_cat(cat_name, tool):
    """
    Чешет кота.
    """
    if tool not in ["щетка", "расческа", "перчатки"]:
        raise ValueError(f"Нельзя чесать кота {cat_name} {tool}")

    print(f"Кот {cat_name} чешется {tool}...")
    try:
        if tool == "перчатки":
            raise ValueError("Кот не любит перчатки!")
        print(f"Кот {cat_name} мурчит")
    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        print(f"Чесание кота {cat_name} завершено")


# 4 задание
def show_cat(cat_name, person):
    """
    Показывает кота
    """
    try:
        if not isinstance(person, str):
            raise TypeError(f"Не получится показать кота {person}")
        print(f"Показываем кота {cat_name} человеку {person}")

        if person == "Олег":
            if random.random() < 0.5:
                raise ValueError(f"Кот поцарапал {person}")
            raise IndexError("Кот залез на шкаф")
        print(f"Кот {cat_name} рад играть с {person}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except IndexError as e:
        print(f"Ошибка индекса: {e}")
    finally:
        print(f"Показ кота {cat_name} завершен")


def squeeze_cat(cat_name, action):
    """
    Пожамкать кота
    """
    try:
        if not isinstance(action, str):
            raise TypeError(f"Нельзя выполнить действие {action}")
        print(f"{action} кота {cat_name}...")

        if action == "пнуть":
            if random.random() < 0.5:
                raise NameError(f"Вас побил хозяим кота {cat_name}")
            raise KeyError(f"Кот {cat_name} увернулся от {action}")
        print(f"Кот {cat_name} доволен!")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except KeyError as e:
        print(f"Ошибка: {e}")
    except NameError as e:
        print(f"Ошибка: {e}")
    finally:
        print(f"Кот {cat_name} вернуля в изначальную форму")


def give_medicine(cat_name, medicine):
    """
    Дать коту лекарство
    """
    try:
        if not isinstance(cat_name, str):
            raise NoCatsError(f"Такое кот {cat_name} не найден")
        if random.random() > 0.5:
            raise HungryCatError(f"{cat_name} не выпил {medicine}, потому что он голоден")
        if medicine == 'парацетомол':
            raise CatError(f"Нельзя давать {medicine} котику {cat_name}")
        print(f"Котик {cat_name} выпил лекарство {medicine} и теперь здоров")
    except NoCatsError as e:
        print(f"Ошибка отсутствия кота: {e}")
    except HungryCatError as e:
        print(f"Ошибка голодного кота: {e}")
    except CatError as e:
        print(f"Ошибка кота: {e}")


# 5 и 7 задание
def count_cats(count, max_value):
    """
    Проверка количнства котов
    """
    try:
        if count == 0:
            raise NoCatsError("Котиков нет")
        if count > max_value:
            raise TooManyCatsError(f"Котов больше {max_value}")
        print(max_value - count)
    except NoCatsError as e:
        print(f"Ошибка отсутствия кота: {e}")
    except TooManyCatsError as e:
        print(f"Ошибка количества котов: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")


# 6 задание
class CatError(Exception):
    """Базовое исключение для ошибок, связанных с котами"""


class TooManyCatsError(CatError):
    """Исключение, если слишком много котов"""


class NoCatsError(CatError):
    """Исключение, если нет котов"""


class HungryCatError(CatError):
    """Исключение, если кот голодный"""
