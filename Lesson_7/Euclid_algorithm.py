def gcd1(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd1(a-b, b)
    else:
        return gcd1(a, b-a)


# print(gcd1(4,7))


def gcd2(a: object, b: object) -> object:
    if b == 0:
        return a
    else:
        return gcd2(b, a%b)


# print(gcd2(3, 8))


def gcd3(a, b):
    return a if b == 0 else gcd3(b, a%b)


print(gcd3(9, 3))