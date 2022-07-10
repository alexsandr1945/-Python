def check_sorted(A, ascending = True):
    """
    Проверка отсортированности за O(len(A))
    :param A:
    :param ascending:
    :return:
    """

    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, N-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag

