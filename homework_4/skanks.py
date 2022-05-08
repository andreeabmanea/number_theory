from Crypto.Util.number import getPrime
from math import ceil, sqrt
import random
from sympy.ntheory.residue_ntheory import primitive_root


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


def skanks_algorithm():
    # p = 13
    # alfa = 2
    # beta = 11
    p = getPrime(32)
    alfa = primitive_root(p)
    beta = random.randint(2, 5000)
    m = ceil(sqrt(p - 1))
    L = []
    for j in range(0, m):
        second = pow(alfa, j, p)
        L.append((j, second))
    seconds = [x[1] for x in L]
    for i in range(len(L)):
        exponent = i * m
        result = modinv(pow(alfa, exponent, p), p)
        new_value = (beta * result) % p
        if new_value in seconds:
            return f"For p = {p}, alfa = {alfa} and beta = {beta}, the result is {i * m + j}"


print(skanks_algorithm())
