def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right



def binary_array_search():
    """
    Бинарный поиск в массиве
    Массив в котором осуществляется поиск должен быть отсортирован
    :return:
    """