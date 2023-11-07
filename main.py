# character_creation_module/main.py

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().


def attack(char_name: str, char_class: str) -> str:
    """Вывод значения атаки."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Вывод значения защиты."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Вывод значения специального умения."""
    ...


def start_training(char_name: str, char_class: str) -> str:
    """Выбор тренировки."""
    ...


def choice_char_class() -> str:
    """Выбор класса персонажа."""
    ...


if __name__ == '__main__':
    """Генерация персонажа. Ввод имени."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
