from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    is_dark_theme = None
    #  переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if current_time.hour < 6 or current_time.hour >= 22:
        is_dark_theme = True

    assert is_dark_theme is True
    print(is_dark_theme)

test_dark_theme_by_time()


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    #  переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = None

    if dark_theme_enabled_by_user == None:
        if current_time.hour < 6 or current_time.hour >= 22:
            is_dark_theme = True
        else:
            is_dark_theme = False
    elif dark_theme_enabled_by_user == True:
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True
    print(is_dark_theme)

test_dark_theme_by_time_and_user_choice()

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users_1 = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users_1 = user
    assert suitable_users_1 == {"name": "Olga", "age": 45}
    print(suitable_users_1)

    # TODO найдите всех пользователей младше 20 лет
    suitable_users_2 = []
    for user in users:
        if user["age"] < 20:
            suitable_users_2.append(user)
    assert suitable_users_2 == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]
    print(suitable_users_2)

test_find_suitable_user()


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def readable(func, *args, **kwargs):
    # имя функции → читаемый вид
    name = func.__name__.replace("_", " ").title()

    # собираем значения аргументов
    values = list(args) + list(kwargs.values())
    values_str = ", ".join(map(str, values))

    result = f"{name} [{values_str}]"
    print(result)
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

readable(test_readable_function)

def open_browser(browser_name):
    actual_result = None
    assert actual_result == "Open Browser [Chrome]"

readable(open_browser)


def go_to_companyname_homepage(page_url):
    actual_result = None
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

readable(go_to_companyname_homepage)

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

readable(find_registration_button_on_login_page)