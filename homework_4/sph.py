from Crypto.Util.number import getPrime
from sympy.ntheory.residue_ntheory import primitive_root
from sympy import sieve, isprime
import random
import math
from skanks import skanks_algorithm, modinv


def get_factorization(max_number):
    factors = [i for i in sieve.primerange(max_number)]
    decomposition = {}
    for i in factors:
        decomposition[i] = {"times": random.randint(1, 5)}
    return decomposition

def garner_algorithm(m: list, v: list):
    m.insert(0, 0)
    v.insert(0, 0)
    c = [0] * len(m)
    for i in range(2, len(m)):
        c[i] = 1
        for j in range(1, i):
            u = modinv(m[j], m[i])
            c[i] = (u * c[i]) % m[i]
    u = v[1]
    x = u
    for i in range(2, len(m)):
        u = ((v[i] - x) * c[i]) % m[i]
        prod = 1
        for j in range(1, i):
            prod *= m[j]
        x = x + u * prod

    return x

def sph_algorithm():

    factors = get_factorization(random.randint(15, 20))
    min_p_minus_1 = 1
    for factor in factors:
        min_p_minus_1 *= pow(factor, factors[factor]["times"])
    min_p = min_p_minus_1 + 1
    while not isprime(min_p):
        factors[2]["times"] += 1
        min_p_minus_1 *= 2
        min_p = min_p_minus_1 + 1
    p = min_p

    alfa = primitive_root(p)
    beta = random.randint(2, 5000)
    for factor in factors.keys():
        new_alfa = pow(alfa, min_p_minus_1 // factor, p)
        factors[factor]["alfa"] = new_alfa

    # factors = {2: {"times": 3, "alfa": 40}, 5: {"times": 1, "alfa": 10}}
    # p = 41
    # alfa = 6
    # beta = 5
    for p_i in factors.keys():
        exponent = (p - 1) // p_i
        log_argument = pow(beta, exponent, p)
        m = math.ceil(math.sqrt(p_i))
        c_0 = 0
        while not pow(factors[p_i]["alfa"], c_0, p) == log_argument % p:
            c_0 += 1
        factors[p_i]["x_i"] = [c_0]
        s_j = c_0
        for j in range(1, factors[p_i]["times"]):
            beta_exponent = (p-1) // pow(p_i, j+1)
            alfa_exponent = ((p-1) // pow(p_i, j+1)) * (-1) * s_j
            new_alfa = pow(alfa, alfa_exponent, p)
            new_beta = pow(beta, beta_exponent, p)
            log_argument = new_alfa * new_beta
            c_j = 0
            while not pow(factors[p_i]["alfa"], c_j, p) == log_argument % p:
                c_j += 1
            factors[p_i]["x_i"].append(c_j)
            s_j += c_j * pow(p_i, j)
    for p_i in factors.keys():
        x_list = factors[p_i]["x_i"]
        power = 0
        current_x = 0
        for digit in x_list:
            current_x += digit * pow(p_i, power)
            power+=1
        factors[p_i]["x"] = current_x
    
    print(factors)

    v = [factors[p_i]["x"] for p_i in factors.keys()]
    m = [pow(p_i, factors[p_i]["times"], p) for p_i in factors.keys()]
    return garner_algorithm(m, v)


print(f"x={sph_algorithm()}")
