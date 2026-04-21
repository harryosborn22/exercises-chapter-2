from math import sqrt, ceil


def isprime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, ceil(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
