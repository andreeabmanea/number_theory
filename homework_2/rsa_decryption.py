from random import randrange
from Crypto.Util.number import getPrime, getRandomInteger


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


def generate_multiprime_parameters():
    p = getPrime(64)
    q = getPrime(64)
    while p == q:
        q = getPrime(64)
    r = getPrime(64)
    while p == r or q == r:
        r = getPrime(64)
    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = getRandomInteger(16)
    while not coprime(e, phi):
        e = getRandomInteger(16)

    return {"p": p, "q": q, "r": r, "n": n, "phi": phi, "e": e}


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


def find_x(y, m, d):

    return pow((y % m), d % (m - 1)) % m


def encrypt_x(x, e, p, q, r):
    phi = (p - 1) * (q - 1) * (r - 1)
    n = p * q * r
    d = modinv(e, phi)
    return (pow(x, e) % n, d)


def decrypt_multipower(x, params):
    print(f"Initial message: x={x}")
    (x_encrypted, key) = encrypt_x(
        x, params["e"], params["p"], params["q"], params["r"]
    )
    print(f"Multipower parameters: {params}")
    x_p = find_x(x_encrypted, params["p"], key)
    x_q = find_x(x_encrypted, params["q"], key)
    x_r = find_x(x_encrypted, params["r"], key)
    v = [x_p, x_q, x_r]
    m = [params["p"], params["q"], params["r"]]
    return garner_algorithm(m, v)


def test_example():
    test_dictionary = {
        "p": 3,
        "q": 5,
        "r": 7,
        "n": 105,
        "phi": 48,
        "e": 11,
    }
    return decrypt_multipower(68, test_dictionary)


print("\tMultipower RSA")
print(f"After multipower decryption: x={test_example()}")

print(decrypt_multipower(68, generate_multiprime_parameters()))
