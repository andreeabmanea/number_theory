from Crypto.Util.number import getPrime
from sympy.ntheory.residue_ntheory import primitive_root
from sympy import sieve, isprime
import random
import math


def get_factorization(max_number):
    factors = [i for i in sieve.primerange(max_number)]
    decomposition = {}
    for i in factors:
        decomposition[i] = random.randint(1, 5)
    return decomposition


def sph_algorithm():

    factors = get_factorization(random.randint(15, 20))
    print(factors)
    min_p_minus_1 = 1
    for factor in factors:
        min_p_minus_1 *= pow(factor, factors[factor])
    min_p = min_p_minus_1 + 1
    while not isprime(min_p):
        factors[2] += 1
        min_p_minus_1 *= 2
        min_p = min_p_minus_1 + 1
    p = min_p
    print(factors)
    
    alfa = primitive_root(p)
    beta = random.randint(2, 5000)
    alfas = []
    for factor in factors.keys():
        new_alfa = pow(alfa, min_p_minus_1 // factor, p)
        alfas.append(new_alfa)
    print(alfas)
    exponent = min_p_minus_1 // next(reversed(factors.keys())) 
    log_argument = pow(beta, exponent, p)
    last_alfa = alfas[-1]
    c_0 = math.log(log_argument, last_alfa)


sph_algorithm()
