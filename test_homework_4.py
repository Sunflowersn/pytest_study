import random

def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)
test_greeting()

def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    #  сосчитайте периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    #  сосчитайте площадь
    area = a * b

    assert area == 200
    print(perimeter)
    print(area)
test_rectangle()

def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    from math import pi
    r = 23
    #  сосчитайте площадь
    area = pi * r**2
    print(area)

    assert area == 1661.9025137490005

    #  сосчитайте длину окружности
    length = 2 * pi * r
    print(length)

    assert length == 144.51326206513048
test_circle()

def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    #  создайте список
    l = random.sample(range(1, 101), 10)
    print(l)
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    print(l)

test_random_list()

def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    #  удалите повторяющиеся элементы
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(l)

test_unique_elements()


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    #  создайте словарь
    d = dict(zip(first, second))
    print(d)

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second

test_dicts()