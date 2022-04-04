from Crypto.Util.number import getPrime
from datetime import datetime
from utils import modinv, find_x, garner_algorithm


def encrypt_x(x, e, p, q):
    phi = (pow(p, 2) - p) * (q - 1)
    n = p * q
    d = modinv(e, phi)
    return (pow(x, e, n), d)


def generate_multipower_parameters():
    p = getPrime(1024)
    q = getPrime(1024)
    while p == q:
        q = getPrime(1024)
    n = p * q
    phi = (pow(p, 2) - p) * (q - 1)
    e = 29

    return {"p": p, "q": q, "n": n, "phi": phi, "e": e}


def hansel_lemma(y, x_0, e, p):
    alfa = (y - (pow(x_0, e, pow(p, 2)))) // p
    temp = e * (pow(x_0, (e - 1), pow(p, 2)) % p)
    x_1 = alfa * (modinv(temp, p))
    return x_1


def decrypt_multipower(x_encrypted, key, params):

    print(f"Multipower parameters: {params}")
    x_q = find_x(x_encrypted, params["q"], key)
    x_p_0 = find_x(x_encrypted, params["p"], key)
    x_p_1 = hansel_lemma(x_encrypted, x_p_0, params["e"], params["p"])
    x_p = x_p_1 * params["p"] + x_p_0
    v = [x_p, x_q]
    m = [params["p"], params["q"]]
    return f"After decryption: x={garner_algorithm(m, v)}"


def time_comparison_multipower(x, params):
    print(f"Initial message: x={x}")
    print()
    (x_encrypted, key) = encrypt_x(x, params["e"], params["p"], params["q"])
    start = datetime.now()
    print(decrypt_multipower(x_encrypted, key, params))
    end = datetime.now()
    print(
        f"Decryption with Garner's Algorithm took {(end - start).total_seconds()} seconds"
    )
    print()
    start = datetime.now()
    n = params["n"]
    print(f"After decryption: x={pow(x_encrypted, key, n)}")
    end = datetime.now()
    print(
        f"Classic decryption with Python library took {(end - start).total_seconds()} seconds"
    )


time_comparison_multipower(43, generate_multipower_parameters())
