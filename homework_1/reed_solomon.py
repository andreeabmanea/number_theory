import random
from Crypto.Util.number import getPrime
from math import *
import itertools


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


def generate_big_prime():
    return getPrime(21)


def convert_decimal_to_base(decimal_number, base):

    decimal_number = int(decimal_number)
    remainders = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainders.append(remainder)
        decimal_number = decimal_number // base

    remainders.reverse()
    remainders.append(0)
    return remainders


def compute_polynom(x, coeficients, p):

    result = coeficients[0]
    for i in range(1, len(coeficients)):

        result = result * x + coeficients[i]

    return result % p


def encode_message(m, p):

    new_m = convert_decimal_to_base(m, p)
    k = len(new_m) + 1
    n = k + 2
    y = []
    for i in range(1, n):
        y.append(compute_polynom(i, new_m, p))
    return y


def alter_y(y: list, p: int):
    error_index = random.randint(1, len(y))
    new_value = random.randint(0, p - 1)
    while new_value == y[error_index]:
        new_value = random.randint(0, p - 1)
    z = y.copy()
    z[error_index] = new_value
    return z


def compute_free_coefficient(z: list, A: list, p: int):
    sum = 0

    for i in A:
        A_without_i = A.copy()
        A_without_i.remove(i)
        product = 1
        for j in A_without_i:
            if (j / (j - i)) == (j // (j - i)):
                fraction = j / (j - i)
            else:
                fraction = j * (modinv((j - i) % 11, 11))
            product = product * fraction
        product = product * z[i]
        sum = sum + product
    return sum % p


def find_all_coefficients(n: int, k: int, z, p, x):
    N = [i for i in range(1, n + 1)]
    subsets = list(itertools.combinations(N, k))
    for A in subsets:
        if int(compute_free_coefficient(z, list(A), p)) == 0:
            print(find_polynom(x, z, list(A), p))


def find_polynom(x: int, z: list, A: list, p: int):
    sum = 0

    for i in A:
        A_without_i = A.copy()
        A_without_i.remove(i)
        product = 1
        for j in A_without_i:
            fraction = (x - j) / (i - j)
            product = product * fraction
        product = product * z[i]
        print(product)
        # think about how to reconstruct polynom
        sum = sum + product
    return sum % p


z = [0, 9, 2, 6, 5, 8]
A = [1, 3, 4]
find_all_coefficients(5, 3, z, 11, 1)