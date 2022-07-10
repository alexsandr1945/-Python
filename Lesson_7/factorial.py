def factorial_calc(n):
    assert n >= 0, " Факториал неопределён"
    if n == 0 :
        return 1
    return factorial_calc(n-1) * n


print(factorial_calc(25))
