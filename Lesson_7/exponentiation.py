def pow_(a, n):
    if n == 0:
        return 1
    else:
        return pow_(a, n-1)*a


# print(pow_(45, 9))

def pow_1(a, n):
    if n == 0:
        return 1
    elif n%2 == 1:
        return pow_1(a, n-1)*a
    else:
        return pow_(a**2, n//2)

print(pow_1(2, 1000))

