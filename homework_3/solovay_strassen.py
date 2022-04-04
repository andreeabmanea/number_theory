import random

from sympy import prime


def test_primality(n: int, t: int):
    if n < 3 or n % 2 == 0 or t < 1:
        raise Exception("Invalid parameters!")
    for i in range(1, t):
        a = random.randint(2, n - 2)
        r = pow(a, (n - 1) / 2, n)
        if r != 1 or r != n - 1:
            return "Composite"
        jacobi_symbol = None
        if r % n != jacobi_symbol % n:
            return "Composite"
        return "Prime"


def compute_jacobi_symbol(a, n):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    # regula de reducere
    if a % n == 0:
        a = a % n
    # regula de multiplicitate
    if is_composite(a):
        list_a = prime_factors(a)


def is_composite(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return True
    return False


import math


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)

    return list(set(factors))


def jacobi(a, n):
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    if n % 2 == 0:
        raise ValueError("'n' must be odd.")
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0


print(jacobi(12, 5))
