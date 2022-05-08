import math
import random
from Crypto.Util.number import getPrime
from datetime import datetime



def test_primality(s: int, method: str = None):
    if s < 3:
        raise Exception("s must be greater than 3")
    n = pow(2, s) - 1
    for i in range(2, math.floor(math.sqrt(s)) + 1):
        if s % i == 0:
            return "Composite"
    u = 4
    for k in range(1, s - 1):
        if method == "course":
            u = modular_reduction((pow(u, 2) - 2), s)
        else:
            u = (pow(u, 2) - 2) % n
    if u == 0:
        return "Prime"
    return "Composite"


def modular_reduction(a, n):
    exp_n = pow(2, n)
    a1 = a // exp_n
    a0 = a % exp_n
    if a0 + a1 < exp_n - 1:
        return a0 + a1
    else:
        return a0 + a1 - (exp_n - 1)


print("Lucas Lehmer Test")
for _ in range(10):
    random_integer = random.randint(3, 50)
    print(
        "Number "
        + str(random_integer)
        + " is "
        + str(
            test_primality(random_integer, "course")
            + " / "
            + str(test_primality(random_integer))
        )
    )


big_prime = getPrime(11)
print(f"n = {pow(2, big_prime) - 1}")
start = datetime.now()
print("n is " + str(test_primality(big_prime, "course")))
end = datetime.now()
seconds_course = (end - start).total_seconds()
print(f"Course algorithm took {seconds_course}")
start = datetime.now()
print("n is " + str(test_primality(big_prime)))
end = datetime.now()
seconds_default = (end - start).total_seconds()

print(f"Default with python took {seconds_default}")
