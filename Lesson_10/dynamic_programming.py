def fib1(n):
    """
    Вычисление числа Фибоначчи с использльзованием рекурсии
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fib1(n-1)+fib1(n-2)

def fib2(n):
    """
    Вычисление числа Фибоначчи методом динамического программирования
    :param n:
    :return:
    """
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


"""
import time
N = int(input('Введите число Фибонначи: '))

for i in range(N):
    start = time.time_ns()
    #print(start)
    print("Значение числа Фибоначчи для  N = ", i, ", fib = ", fib2(i), sep=' ', end= ' ')
    print('Время вычисления = ', (time.time_ns()-start))
"""
def traj_num(n):
    """
    Одномерное динамическое программирование
    Вычисление количества траекторий из 1 в N
    Возможные шаги +1 и +2
    :return:
    """
    k=[0, 1] + [0]*n
    for i in range(2, n+1):
        k[i] = k[i-1] + k[i-2]
    return k[n]

def count_traj(n, allowed:list):
    """
    Одномерное динамическое программирование
    Вычисление количества траекторий из 1 в N
    Возможные шаги +1, +2, +3 есть точки которые посещать нельзя
    :return:
    """
    k = [0, 1, int(allowed[2])]+[0]*(n-3)
    for i in range(3, n+1):
        if allowed[i]:
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[n]

def count_min_coast(n, price:list):
    """
    Минимальная стоимость достижения клетки n
    price[i] - цена за посещение i-й клетки
    C[i] - минимальная стоимость достижения клетки
    :return:
    """

    C=[float("-inf"), price[1], price[1] + price[2]] + [0] * (n-2)
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]

