def is_simple_number(x):
    """
    Определяет, является ли число простым.
    :return: True, если число простое. False - если иначе.
    """

    divisor = 2  # Задаём начальное значение делителя.
    while divisor < x:
        if x % divisor == 0:
            return x, False
        divisor += 1
    return x, True


def factorize_number(x):
    """
    Раскладывает число на множители. Выводит множители на экран.
    :param x: целое положительное число.
    :return:
    """

    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor, end=' ')
            x //= divisor
        else:
            divisor += 1


x = int(input("Введите число: "))
# print(is_simple_number(x))
factorize_number(x)
