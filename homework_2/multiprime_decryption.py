from Crypto.Util.number import getPrime
from datetime import datetime
from utils import modinv, find_x, garner_algorithm


def generate_multiprime_parameters():
    p = getPrime(512)
    q = getPrime(512)
    while p == q:
        q = getPrime(512)
    r = getPrime(512)
    while p == r or q == r:
        r = getPrime(512)
    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = 29

    return {"p": p, "q": q, "r": r, "n": n, "phi": phi, "e": e}


def encrypt_x(x, e, p, q, r):
    phi = (p - 1) * (q - 1) * (r - 1)
    n = p * q * r
    d = modinv(e, phi)
    return (pow(x, e, n), d)


def decrypt_multiprime(x_encrypted, key, params):

    print(f"Multiprime parameters: {params}")
    x_p = find_x(x_encrypted, params["p"], key)
    x_q = find_x(x_encrypted, params["q"], key)
    x_r = find_x(x_encrypted, params["r"], key)
    v = [x_p, x_q, x_r]
    m = [params["p"], params["q"], params["r"]]
    return f"After decryption: x={garner_algorithm(m, v)}"


def time_comparison_multiprime(x, params):
    print(f"Initial message: x={x}")
    print()
    (x_encrypted, key) = encrypt_x(
        x, params["e"], params["p"], params["q"], params["r"]
    )
    start = datetime.now()
    print(decrypt_multiprime(x_encrypted, key, params))
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


if __name__ == "__main__":
    time_comparison_multiprime(68, generate_multiprime_parameters())
# Course example
# time_comparison(68, {"p": 3, "q": 5, "r": 7, "n": 105, "phi": 48, "e": 11})
