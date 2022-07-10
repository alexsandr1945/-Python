def lcs(A, B):
    """
    Вычисление наибольшей общей последовательности
    :param A:
    :param B:
    :return:
    """

    F =[[0] * len(B)+1 for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B [j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    return F[-1][-1]
def gis(A):
    """
    Вычислени наибольшей возрастающей подпоследовательности

    F[i] - наибольшая возрастающая подпоследовательность для части A[0:i],
    которая заканчивается и содержит элемент a[i]=A[i-1]
    F[i]=max(F[j])+1, j<i,a[i]>a[j]
    Крайний случай
    F[0]=0

    :return:
    """
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        m = 0
        for j in range(0, i):
            if A[i] > A[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]