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


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def coprime(x, y):
    return gcd(x, y) == 1


def find_x(y, m, d):

    return pow((y % m), d % (m - 1), m)


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


def convert_decimal_to_base(decimal_number, base):

    decimal_number = int(decimal_number)
    remainders = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainders.append(remainder)
        decimal_number = decimal_number // base

    remainders.reverse()
    return remainders

