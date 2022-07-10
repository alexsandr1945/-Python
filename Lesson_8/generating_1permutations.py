def generating_permutations(N:int, M:int, prefix=None):
    """
    Генерируются все числа с лидирующими незначащими нулями в N - ричной системе счисления (N < = 10)
    длины M
    :param N:
    :param M:
    :param prefix:
    :return:
    """

    prefix = prefix or []
    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        generating_permutations(N, M-1, prefix)
        prefix.pop()


#generating_permutations(3,3)


def find_number(number, A):
    """
    Функция ищет x в A
    :param x:
    :param A:
    :return: возвращае True,если есть, False, если нет.
    """

    for x in A:
        if number == x:
            return True
    return False


def generating_permutations_all(N:int, M:int=-1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях с префиксом prefix
    :param N:
    :param M:
    :param prefix:
    :return:
    """

    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []

    if M == 0:
        print(*prefix, end=',', sep='')
        return

    for number in range(1, N+1):
        if find_number(number,prefix):
            continue
        prefix.append(number)
        generating_permutations_all(N, M-1, prefix)
        prefix.pop()


generating_permutations_all(5)