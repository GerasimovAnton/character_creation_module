from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Number: int) -> int:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: int) -> int:
    """Сравниваем число с 0."""
    if your_number <= 0:
        return
    num = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {num}')


print(message)
calc(25.5)
