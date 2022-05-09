from Crypto.Util.number import getPrime
from math import ceil, sqrt, floor
import random
from sympy import isprime


def jacobi(a, n):
    if n <= 0:
        raise Exception("n must be positive")
    if n % 2 == 0:
        raise Exception("n must be odd")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a = a / 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    if n == 1:
        return result
    else:
        return 0


def generate_quadratic_non_residue(p):
    if p % 4 == 3:
        return -1
    if p % 8 == 5:
        return 2
    while True:
        a = random.randint(1, p)
        if jacobi(a, p) == -1:
            return a


def get_odd_prime_factors(x):
    factors = []
    for i in range(3, int(floor(sqrt(x)))):
        if int(x) % i == 0:
            if i % 2 == 1 and isprime(i):
                factors.append(i)
                if isprime(x // i) and x // i % 2 == 1:
                    factors.append(x//i) 
    return factors


def primitive_root(p):
    alfa = generate_quadratic_non_residue(p)
    ok = 1
    odd_primes = get_odd_prime_factors(p - 1)
    for r in odd_primes:
        if pow(alfa, (p - 1) // r) == 1:
            ok = 0
    if ok == 1:
        return alfa


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


def skanks_algorithm(p, alfa, beta, m):
    # p = 13
    # alfa = 2
    # beta = 11
    # p = getPrime(32)
    # alfa = primitive_root(p)
    # beta = random.randint(2, 5000)
    # m = ceil(sqrt(p - 1))  # parte intreaga superioara din radical din pi
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
            return i * m + j


# print(skanks_algorithm())
